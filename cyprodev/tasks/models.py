from django.conf import settings
from django.db import models

# Create your models here.


class Task(models.Model):
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='assigned_user', on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='admin', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.task
