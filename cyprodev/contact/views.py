from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactForm, ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
