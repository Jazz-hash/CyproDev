from django.db import models
from django.conf import settings
from django.urls import reverse
from services.models import Service
# Create your models here.


class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    hosted_link = models.URLField(blank=True)
    filter = models.CharField(max_length=10, blank=True)
    header_image = models.ImageField(upload_to='portfolio-images', blank=True)
    category = models.ForeignKey(
        Service, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:add')

    def save(self, *args, **kwargs):
        self.filter = self.category.head[:2].lower()
        super().save(*args, **kwargs)


class Image(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, default=None, related_name='porfolio_images')
    image = models.ImageField(upload_to='portfolio-images', blank=True)

    def __str__(self):
        return self.portfolio.name
