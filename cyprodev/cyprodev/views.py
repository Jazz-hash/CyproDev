from django import views
from django.shortcuts import render
from django.views.generic import (TemplateView)


class Index(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['head'] = 'Home'
        context['slider_head'] = 'We Are Cyprodev'
        context['slider_sub_head'] = 'We make your market digitally we make your ideas come true we build your startups we design we develop'
        return context


class About(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['head'] = 'About'
        context['slider_head'] = 'About Us'
        context['slider_sub_head'] = 'Lorem'

        return context


class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['head'] = 'Dashboard'
        return context
