"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from services.views import ServiceHomeListView
from contact.views import (
    ContactCreateView, ProjectCreateView, ProjectListView, ProjectDetailView)
from accounts.views import UserDetailsEditView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from portfolio.views import PortfolioPublicListView, PortfolioPublicDetailView
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('our-services/', ServiceHomeListView.as_view(), name="services"),
    path('portfolios/', PortfolioPublicListView.as_view(), name="portfolios"),
    path('portfolios/<int:pk>',
         PortfolioPublicDetailView.as_view(), name="portfolios_detail"),
    path('contact-us/', ContactCreateView.as_view(), name="contact"),
    path('start-your-project/', ProjectCreateView.as_view(),
         name="start-your-project"),
    path('dashboard/', UserDetailsEditView, name="dashboard"),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('services/', include('services.urls', namespace='services')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('task/', include('tasks.urls', namespace='task')),
    path('project/', ProjectListView.as_view(), name='projects'),
    path('project/details/<int:pk>/',
         ProjectDetailView.as_view(), name='project_details'),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('api/user/', include('accounts.api.urls', namespace='accounts-api')),
    path('api/portfolio/', include('portfolio.api.urls', namespace='portfolio-api')),
    path('api/service/', include('services.api.urls', namespace='service-api')),
    path('api/tasks/', include('tasks.api.urls', namespace='task-api')),
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
    path('notifications/detail/<int:pk>',
         views.NotificationDetailView.as_view(), name="notify_details"),
    path('notifications/',
         views.NotificationListView.as_view(), name="notify"),
]
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT))
