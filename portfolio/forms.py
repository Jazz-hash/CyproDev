from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control mb-2'}))
    header_image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = Portfolio
        fields = ['name', 'category', 'language',
                  'description','header_image', 'images', 'hosted_link']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'language': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'hosted_link': forms.URLInput(attrs={'class': 'form-control mb-2'}),
        }
