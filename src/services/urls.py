from django.urls import path
from .views import (ServiceListView, ServiceDetailView,
                    ServiceCreateView, ServiceUpdateView, ServiceDeleteView)
app_name = 'services'

urlpatterns = [
    path('', ServiceListView.as_view(), name='list'),
    path('add/', ServiceCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', ServiceUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/', ServiceDetailView.as_view(), name='details'),
]
