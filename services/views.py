from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Service
from .forms import ServiceModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cyprodev.mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'List'
        return context


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Details'
        return context


class ServiceCreateView(LoginRequiredMixin, UserPassesTestMixin, FormUserNeededMixin, CreateView):
    form_class = ServiceModelForm
    template_name = 'services/services_add.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'New'
        return context

    def test_func(self):
        return self.request.user.is_superuser


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UserOwnerMixin, UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'services/services_edit.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Edit'
        return context

    def test_func(self):
        return self.request.user.is_superuser


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    success_url = 'services:list'

    def get_context_data(self, **kwargs):
        context = super(ServiceDeleteView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['sub_head'] = 'Remove'
        return context

    def test_func(self):
        return self.request.user.is_superuser


class ServiceHomeListView(ListView):
    model = Service
    template_name = "home/services.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceHomeListView, self).get_context_data(**kwargs)
        context['head'] = 'Services'
        context['slider_head'] = 'Services'
        context['slider_sub_head'] = 'We are providing wide range of services by our tremendous team. You can check details of every service that we have.'
        context['slider_image'] = '/static/static/img/services.jpg'

        return context
