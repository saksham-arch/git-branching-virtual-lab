import csv
import io
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from .catalog import EXPERIMENTS
from .forms import CSVForm, ObservationForm, RegistrationForm
from .models import Observation
from .services import csv_cell, import_csv


def index(request):
    return render(request, 'course/index.html', {'experiments': EXPERIMENTS})


def experiment(request, slug):
    item = next((x for x in EXPERIMENTS if x['slug'] == slug), None)
    if item is None:
        from django.http import Http404
        raise Http404('Experiment not found')
    score = None
    if request.method == 'POST':
        answers = [request.POST.get(f'q{i}') for i in range(len(item['questions']))]
        score = sum(a == str(q['answer']) for a, q in zip(answers, item['questions']))
    return render(request, 'course/experiment.html', {'experiment': item, 'score': score})


class TemplateLab(TemplateView):
    template_name = 'course/template_lab.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(name=self.request.GET.get('name', 'Student')[:80], values=[4, 8, 12])
        return context


def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.save())
        return redirect('course:observations')
    return render(request, 'course/form.html', {'form': form, 'title': 'User registration'})


@login_required
def observations(request):
    instance = None
    if request.GET.get('edit'):
        instance = get_object_or_404(Observation, pk=request.GET['edit'], owner=request.user)
    form = ObservationForm(request.POST or None, instance=instance, initial={'value': 10})
    if request.method == 'POST' and form.is_valid():
        observation = form.save(commit=False)
        observation.owner = request.user
        observation.save()
        messages.success(request, 'Observation saved.')
        return redirect('course:observations')
    rows = list(Observation.objects.filter(owner=request.user))
    maximum = max((row.value for row in rows), default=1) or 1
    for row in rows:
        row.width = float(row.value / maximum * 100)
    return render(request, 'course/observations.html', {'form': form, 'rows': rows, 'csv_form': CSVForm()})


@login_required
def delete_observation(request, pk):
    row = get_object_or_404(Observation, pk=pk, owner=request.user)
    if request.method == 'POST':
        row.delete()
        return redirect('course:observations')
    return render(request, 'course/delete.html', {'row': row})


@login_required
def upload_csv(request):
    form = CSVForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        try:
            count = import_csv(form.cleaned_data['file'], request.user)
            messages.success(request, f'Imported {count} observations.')
            return redirect('course:observations')
        except ValidationError as exc:
            form.add_error('file', exc)
    return render(request, 'course/form.html', {'form': form, 'title': 'Import observations'})


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="observations.csv"'
    writer = csv.writer(response)
    writer.writerow(['title', 'value', 'notes'])
    for row in Observation.objects.filter(owner=request.user):
        writer.writerow([csv_cell(row.title), row.value, csv_cell(row.notes)])
    return response


@login_required
def export_pdf(request):
    from reportlab.pdfgen import canvas
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle('Laboratory observations')
    y = 800
    pdf.drawString(40, y, 'Django laboratory — observations')
    for row in Observation.objects.filter(owner=request.user):
        y -= 24
        if y < 50:
            pdf.showPage()
            y = 800
        pdf.drawString(40, y, f'{row.title}: {row.value}'[:110])
    pdf.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='observations.pdf')


@permission_required('course.export_observation', raise_exception=True)
def instructor_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="class-observations.csv"'
    writer = csv.writer(response)
    writer.writerow(['student', 'title', 'value'])
    for row in Observation.objects.select_related('owner'):
        writer.writerow([csv_cell(row.owner.username), csv_cell(row.title), row.value])
    return response
