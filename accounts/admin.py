from django.contrib import admin
from . models import Profile, UserLog
# Register your models here.
admin.site.site_header = "CyproDev"
admin.site.register(Profile)
admin.site.register(UserLog)
