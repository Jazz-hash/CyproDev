from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FeedbackForm

from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
class FeedbackView(CreateView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = '/feedback/'

    def form_valid(self, form):
        bio = self.request.POST.get('ratings')
        print(bio)
        feedbackForm.rating = bio
        feedbackForm.name = self.request.POST.get('ratings')
        feedbackForm.email = self.request.POST.get('ratings')
        feedbackForm.designation = self.request.POST.get('ratings')
        feedbackForm.company = self.request.POST.get('ratings')
        feedbackForm.message = self.request.POST.get('ratings')
        feedbackForm.save()
        messages.success(
            self.request, "Thank you for your feedback !!")
        return HttpResponseRedirect('/feedback/')
    
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['head'] = 'Feedback'
        context['slider_head'] = 'Feedback'
        context['slider_sub_head'] = 'Mistakes should be examined, learned from, and discarded, Not dwelled upon and stored.'
        return context

