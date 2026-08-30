from django.urls import path
from . import views

app_name = "lab"
urlpatterns = [
    path("", views.experiment, name="experiment"),
    path("api/experiment/", views.experiment_api, name="experiment-api"),
    path("health/", views.health, name="health"),
]
