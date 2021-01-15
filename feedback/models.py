from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    to_be_filtered = models.BooleanField(default=True)

    def __str__(self):
        return self.name