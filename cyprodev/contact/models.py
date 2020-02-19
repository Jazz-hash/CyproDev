from django.db import models
from django.urls import reverse
from services.models import Service
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('home')


class Project(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, default=None)
    details = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('home')
