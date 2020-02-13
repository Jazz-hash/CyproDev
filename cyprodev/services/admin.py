from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


admin.site.register(Service, ServiceModelAdmin)
