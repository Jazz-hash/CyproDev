from django.urls import path
from .views import PortfolioListApiView
from django.conf.urls import url
app_name = 'portfolio-api'
urlpatterns = [
    url(r'^search/$',
        PortfolioListApiView.as_view(), name='list'),

]
