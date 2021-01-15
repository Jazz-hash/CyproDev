from django import views
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import Notification
from feedback.models import Feedback


class Index(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['head'] = 'Home'
        context["object_list"] = Feedback.objects.filter(to_be_filtered=True)
        context['slider_head'] = 'We Are Awesome'
        context['extra_slider_head'] = 'Agency'
        context['slider_sub_head'] = "We are your one stop solution for all your digital marketing and software needs based in Pakistan which is fueled by young and dynamic people. We believe in building strong brands through our clean and creative designs, well-crafted content and integrated strategies. From digital marketing to website development and all your software needs; we're more than just another agency. We're your next business partner."
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
        context['slider_sub_head'] = 'We are Cyprodev. A web, software design and development professionals who love partnering with good people and businesses to help them achieve digital success.'
        return context


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['head'] = 'Dashboard'
        return context
