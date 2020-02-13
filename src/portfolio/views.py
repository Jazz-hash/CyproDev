from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PortfolioForm
from app.mixins import FormUserNeededMixin
from .models import Portfolio, Images
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.


class FileFieldView(FormUserNeededMixin, CreateView):
    form_class = PortfolioForm
    template_name = 'portfolio/portfolio_add.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('name')
        language = request.POST.get('language')
        description = request.POST.get('description')
        hosted_link = request.POST.get('hosted_link')
        print([name, language, description, hosted_link])
        images = request.FILES.getlist('images')
        print(form)
        print(images)

        if form.is_valid():
            # print(form.id)
            portfolio_form = Portfolio.objects.create(user=request.user)
            portfolio_form.name = name
            portfolio_form.language = language
            portfolio_form.description = description
            portfolio_form.hosted_link = hosted_link
            portfolio_form.save()
            print(portfolio_form.id)
            for image in images:
                image_form = Images.objects.create(protfolio=portfolio_form)
                image_form.image = image
                image_form.save()

            return HttpResponse('dada')
        else:
            return self.form_invalid(form)
