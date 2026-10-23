from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Observation, User


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'roll_number')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if not email:
            raise forms.ValidationError('Enter an email address for password recovery.')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ('title', 'value', 'notes')
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Response time'}),
                   'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the measurement'})}

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError('Use at least three characters.')
        return title

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 0:
            raise forms.ValidationError('The measurement must be zero or greater.')
        return value


class CSVForm(forms.Form):
    file = forms.FileField(help_text='UTF-8 CSV, title,value,notes columns. Maximum 1 MB and 500 rows.')
