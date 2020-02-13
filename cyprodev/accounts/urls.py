from django.urls import path
from .views import (ProfileView, UserRegisterView, multiple_forms)
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('<int:pk>/', UserDetailView.as_view(), name='details'),
    path('profile/', multiple_forms, name='profile'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    # path('profile/', auth_views..as_view(), name='profile'),

]
