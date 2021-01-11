from django.contrib import admin
from .models import Service
# Register your models here.

def remove_filter(modeladmin, request, queryset):
    queryset.update(to_be_filtered=False)

def add_filter(modeladmin, request, queryset):
    queryset.update(to_be_filtered=True)

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ["head", "to_be_filtered"]

    actions = [add_filter, remove_filter]


admin.site.register(Service, ServiceModelAdmin)
