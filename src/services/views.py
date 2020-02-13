from django.shortcuts import render
from app.mixins import FormUserNeededMixin, UserOwnerMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Service
from .forms import ServiceModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ServiceListView(ListView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'List'
        return context


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Details'
        return context


class ServiceCreateView(FormUserNeededMixin, CreateView):
    form_class = ServiceModelForm
    template_name = 'services/services_add.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'New'
        return context


class ServiceUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'services/services_edit.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Edit'
        return context


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = 'services:list'

    def get_context_data(self, **kwargs):
        context = super(ServiceDeleteView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Remove'
        return context


class ServiceHomeListView(ListView):
    model = Service
    template_name = "home/services.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceHomeListView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['slider_head'] = 'Services'
        context['slider_sub_head'] = 'Lorem'
        return context
