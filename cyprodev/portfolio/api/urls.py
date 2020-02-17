from django.urls import path
from .views import PortfolioListApiView
app_name = 'portfolio-api'
urlpatterns = [
    path('', PortfolioListApiView.as_view(), name='list'),

]
