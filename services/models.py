from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Service(models.Model):
    icon = models.ImageField(upload_to="services-icons", blank=True)
    head = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    to_be_filtered = models.BooleanField(default=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    filter = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        self.filter = self.head[:2].lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.head

    def get_absolute_url(self):
        return reverse('services:details', kwargs={'pk': self.pk})
