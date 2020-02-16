from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = '/contact'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Contact'
        context['slider_head'] = 'Contact Us'
        context['slider_sub_head'] = 'Lorem'

        return context
