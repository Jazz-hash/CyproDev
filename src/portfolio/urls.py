from django.urls import path
from .views import (FileFieldView)
app_name = 'portfolio'

urlpatterns = [
    # path('', ServiceListView.as_view(), name='list'),
    path('add/', FileFieldView.as_view(), name='add'),

]
