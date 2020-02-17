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
from contact.views import ContactCreateView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from portfolio.views import PortfolioPublicListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('our-services/', ServiceHomeListView.as_view(), name="services"),
    path('portfolios/', PortfolioPublicListView.as_view(), name="portfolios"),
    path('contact/', ContactCreateView.as_view(), name="contact"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('services/', include('services.urls', namespace='services')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('api/user/', include('accounts.api.urls', namespace='accounts-api')),
    path('api/portfolio/', include('portfolio.api.urls', namespace='portfolio-api')),

]
if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT))
    urlpatterns += (static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT))
