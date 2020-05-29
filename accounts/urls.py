from django.urls import path
from .views import (ProfileView, UserRegisterView,
                    UserDetailsEditView, UserLogListView, UserLogDetailView)
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('profile/', UserDetailsEditView, name='profile'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('user-log/', UserLogListView.as_view(), name='user_log'),
    path('user-log/details/<int:pk>',
         UserLogDetailView.as_view(), name='user_log_details'),
]
