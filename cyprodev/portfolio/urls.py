from django.urls import path
from .views import (PortfolioCreateView, PortfolioListView,
                    PortfolioDeleteView, UnderConstruction)
app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='list'),
    path('add/', PortfolioCreateView.as_view(), name='add'),
    # path('edit/<int:pk>/', ServiceUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PortfolioDeleteView.as_view(), name='delete'),
    # path('details/<int:pk>/', ServiceDetailView.as_view(), name='details'),

]
