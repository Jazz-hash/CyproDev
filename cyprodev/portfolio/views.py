from django.shortcuts import render
from django.views.generic import (
    CreateView, TemplateView, ListView, DeleteView)
from .forms import PortfolioForm
from cyprodev.mixins import FormUserNeededMixin
from .models import Portfolio, Image
from services.models import Service
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PortfolioListView(ListView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'List'
        return context


class PortfolioDeleteView(DeleteView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioDeleteView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'List'
        context['images_data'] = Image.objects.filter(portfolio=model)
        return context


class UnderConstruction(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/under.html'

    def get_context_data(self, **kwargs):
        context = super(UnderConstruction, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'List'
        return context


class PortfolioCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = PortfolioForm
    template_name = 'portfolio/portfolio_add.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioCreateView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'Add'
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('name')
        language = request.POST.get('language')
        description = request.POST.get('description')
        hosted_link = request.POST.get('hosted_link')
        category = request.POST.get('category')
        images = request.FILES.getlist('images')
        print('-----------------', category)
        print('-----------------', Service.objects.get(pk=category))

        if form.is_valid():
            print('312312222222222222222222222222')
            portfolio_form = Portfolio.objects.create(
                user=request.user, category=Service.objects.get(pk=category))
            portfolio_form.name = name
            portfolio_form.language = language
            portfolio_form.description = description
            portfolio_form.hosted_link = hosted_link
            portfolio_form.category_id = category
            portfolio_form.save()
            print(portfolio_form.id)
            for image in images:
                image_form = Image.objects.create(protfolio=portfolio_form)
                image_form.image = image
                image_form.save()

            return HttpResponseRedirect('/home')
        else:
            return self.form_invalid(form)
