from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'course'
urlpatterns = [
    path('react/', TemplateView.as_view(template_name='course/react.html'), name='react'),
    path('', views.index, name='index'),
    path('experiments/<slug:slug>/', views.experiment, name='experiment'),
    path('templates/', views.TemplateLab.as_view(), name='templates'),
    path('register/', views.register, name='register'),
    path('observations/', views.observations, name='observations'),
    path('observations/<int:pk>/delete/', views.delete_observation, name='delete'),
    path('csv/import/', views.upload_csv, name='import'),
    path('csv/export/', views.export_csv, name='export'),
    path('pdf/', views.export_pdf, name='pdf'),
    path('instructor/export/', views.instructor_export, name='instructor-export'),
]
