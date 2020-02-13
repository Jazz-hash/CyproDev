from django.urls import path
from .views import (FileFieldView,UnderConstruction)
app_name = 'portfolio'

urlpatterns = [
    path('', UnderConstruction.as_view(), name='list'),

    path('add/', FileFieldView.as_view(), name='add'),

]
