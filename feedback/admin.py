from django.contrib import admin
from .models import Feedback
# Register your models here.


def remove_filter(modeladmin, request, queryset):
    queryset.update(to_be_filtered=False)

def add_filter(modeladmin, request, queryset):
    queryset.update(to_be_filtered=True)

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ["name", "message", "rating", "company", "to_be_filtered"]
    list_filter = ["company", "rating"]

    actions = [add_filter, remove_filter]


admin.site.register(Feedback, FeedbackModelAdmin)
