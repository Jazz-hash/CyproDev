from django.urls import path
from .views import ServiceListApiView
app_name = 'services-api'
urlpatterns = [
    path('', ServiceListApiView.as_view(), name='list'),

]
