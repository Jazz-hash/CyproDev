from django.contrib.auth.signals import user_logged_in, user_logged_out
import datetime
import logging
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='user-images', blank=True)
    social = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.user.username


class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        notify.send(instance, recipient=instance, verb='was saved')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# for logging - define "error" named logging handler and logger in settings.py
error_log = logging.getLogger('error')


@receiver(user_logged_in)
def log_user_logged_in(sender, user, request, **kwargs):
    try:
        login_logout_logs = UserLog.objects.filter(
            session_key=request.session.session_key, user=user.id)[:1]
        if not login_logout_logs:
            login_logout_log = UserLog(login_time=datetime.datetime.now(
            ), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception:
        # log the error
        error_log.error(
            "log_user_logged_in request: %s, error: %s" % (request))


@receiver(user_logged_out)
def log_user_logged_out(sender, user, request, **kwargs):
    try:
        login_logout_logs = UserLog.objects.filter(
            session_key=request.session.session_key, user=user.id, host=request.META['HTTP_HOST'])
        login_logout_logs.filter(logout_time__isnull=True).update(
            logout_time=datetime.datetime.now())
        if not login_logout_logs:
            login_logout_log = UserLog(logout_time=datetime.datetime.now(
            ), session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
    except Exception:
        # log the error
        error_log.error(
            "log_user_logged_out request: %s, error: %s" % (request))
