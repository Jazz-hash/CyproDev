from django.shortcuts import render
from django.views.generic import View
from .forms import FeedbackForm
from .models import Feedback

from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
class FeedbackView(View):
    # form_class = FeedbackForm

    def get(self, *args, **kwargs):
        form = FeedbackForm()
        context = {
            'form': form,
            'head': 'Feedback',
            'slider_head' : 'Feedback',
            'slider_sub_head' : 'Mistakes should be examined, learned from, and discarded, Not dwelled upon and stored.'
        }
        return render(self.request, "feedback/feedback.html", context)

    def post(self, *args, **kwargs):
        form = FeedbackForm(self.request.POST or None)
        context = {
            'form': form,
            'head': 'Feedback',
            'slider_head' : 'Feedback',
            'slider_sub_head' : 'Mistakes should be examined, learned from, and discarded, Not dwelled upon and stored.'
        }
        if form.is_valid():
            rating = self.request.POST.get('ratings')
            print(form, rating)
            feedback = Feedback(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                designation = form.cleaned_data["designation"],
                company = form.cleaned_data["company"],
                message = form.cleaned_data["message"],
                rating = rating
            )
            feedback.save()
            messages.success(self.request, "Thank you for your feedback !!")
            return HttpResponseRedirect('/feedback/')
        else:
            messages.error(
                self.request, "Please fill in the required fields")
        return render(self.request, "feedback/feedback.html", context)


    # def form_valid(self, form):
    #     form.cleaned_data["rating"] = 
    #     print(form.cleaned_data)
    #     form.save()
    #     messages.success(
    #         self.request, "Thank you for your feedback !!")
    #     return HttpResponseRedirect('/feedback/')

    
    # def get_context_data(self, **kwargs):
    #     context = super(FeedbackView, self).get_context_data(**kwargs)
    #     return context

