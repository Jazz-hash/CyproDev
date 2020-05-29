from django.urls import path
from .views import (TasksListView, TasksCreateView,
                    TasksUpdateView, TasksDeleteView, TasksDetailView)
app_name = 'task'

urlpatterns = [
    path('', TasksListView.as_view(), name='list'),
    path('add/', TasksCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', TasksUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', TasksDeleteView.as_view(), name='delete'),
    path('details/<int:pk>/', TasksDetailView.as_view(), name='details'),
]
