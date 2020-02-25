from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('task:details', kwargs={'pk': self.pk})


@receiver(post_save, sender=Task)
def my_handler(sender, instance, **kwargs):
    print(sender)
    print(instance.assigned_to)
    notify.send(instance.user, recipient=instance.assigned_to, description=instance.id,
                verb=f'A new task "{instance.task}" is assigned to you by admin "{instance.user}"')
