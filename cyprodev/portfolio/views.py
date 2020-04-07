from django.shortcuts import render
from django.views.generic import (
    CreateView, TemplateView, ListView, DeleteView, DetailView)
from .forms import PortfolioForm
from cyprodev.mixins import FormUserNeededMixin
from .models import Portfolio, Image
from services.models import Service
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PortfolioPublicListView(TemplateView):
    model = Portfolio
    template_name = 'portfolio/portfolios.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioPublicListView,
                        self).get_context_data(**kwargs)
        context['head'] = 'Portfolios'
        context['slider_head'] = 'Portfolio'
        context['slider_sub_head'] = ''
        context['slider_image'] = '/static/static/img/portfolio.jpg'

        return context


class PortfolioPublicDetailView(DetailView):
    template_name = 'portfolio/portfolios_detail.html'
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioPublicDetailView,
                        self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['slider_head'] = 'Portfolio Detail'
        context['slider_image'] = '/static/static/img/portfolio.jpg'

        return context


class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio

    def get_queryset(self):
        queryset = super(PortfolioListView, self).get_queryset()
        if self.request.user.is_superuser:
            queryset = Portfolio.objects.all()
        else:
            queryset = Portfolio.objects.filter(user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'List'
        return context


class PortfolioDeleteView(LoginRequiredMixin, DeleteView):
    model = Portfolio
    select_related = ('images')

    def get_context_data(self, **kwargs):
        context = super(PortfolioDeleteView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'Remove'
        return context


class PortfolioDetailView(LoginRequiredMixin, DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        context['head'] = 'Portfolio'
        context['sub_head'] = 'Details'
        return context


class PortfolioCreateView(LoginRequiredMixin, CreateView):
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

        if form.is_valid():
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
