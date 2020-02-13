from django.urls import path
from .views import (ProfileUpdateApiView)
app_name = 'accounts-api'
urlpatterns = [
    path('update/<int:pk>', ProfileUpdateApiView.as_view(), name='create'),

]
