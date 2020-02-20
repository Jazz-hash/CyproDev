from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .forms import ContactForm, ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact, Project
# Create your views here.


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Contact'
        context['slider_head'] = 'Contact Us'
        context['slider_sub_head'] = 'Lorem'

        return context


class ContactListView(ListView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        context['head'] = 'Contact Requests'
        context['sub_head'] = 'List'
        return context


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Contact Requests'
        context['sub_head'] = 'Details'
        return context


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Project Requests'
        context['sub_head'] = 'Details'
        return context


class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['head'] = 'Project Requests'
        context['sub_head'] = 'List'
        return context


class ProjectCreateView(CreateView):
    form_class = ProjectForm
    template_name = 'contact/project_form.html'
    success_url = '/start-your-project/'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Start Your Project'
        context['slider_head'] = 'Start Your Project'
        context['slider_sub_head'] = 'Lorem'

        return context
