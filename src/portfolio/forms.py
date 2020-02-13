from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Portfolio
        fields = ['name', 'language', 'description', 'images', 'hosted_link']
