from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=20)
    head = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.head

    def get_absolute_url(self):
        return reverse('services:details', kwargs={'pk': self.pk})
