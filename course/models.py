from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    roll_number = models.CharField(max_length=24, blank=True)


class Observation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        permissions = [('export_observation', 'Can export all observations')]

    def __str__(self):
        return self.title
