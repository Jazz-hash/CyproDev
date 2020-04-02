from django import views
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import Notification


class Index(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['head'] = 'Home'
        context['slider_head'] = 'We Are Cyprodev'
        context['slider_sub_head'] = 'A single place to share, curate and discover visual that tells a story.'
        return context


class NotificationDetailView(DetailView):
    model = Notification
    template_name = "dashboard/notifications_detail.html"

    def get_context_data(self, **kwargs):
        context = super(NotificationDetailView,
                        self).get_context_data(**kwargs)
        context['head'] = 'Notification'
        context['sub_head'] = 'Details'
        return context


class NotificationListView(ListView):
    model = Notification
    template_name = "dashboard/notifications.html"

    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)
        context['head'] = 'Notification'
        context['sub_head'] = 'List'
        return context


class About(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['head'] = 'About'
        context['slider_head'] = 'About Us'
        context['slider_sub_head'] = 'Lorem'

        return context


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['head'] = 'Dashboard'
        return context
