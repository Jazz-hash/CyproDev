from django.urls import path
from .views import (ContactListView, ContactDetailView)
app_name = 'contact'

urlpatterns = [
    path('', ContactListView.as_view(), name='list'),
    path('details/<int:pk>/', ContactDetailView.as_view(), name='details'),

]
