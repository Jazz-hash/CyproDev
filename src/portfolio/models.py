from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    hosted_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:add')


class Images(models.Model):
    protfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='portfolio-images', blank=True)
