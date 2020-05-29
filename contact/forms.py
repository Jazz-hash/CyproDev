from django import forms
from .models import Contact, Project


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'email', 'service', 'details']
