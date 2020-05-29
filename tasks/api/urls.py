from django.urls import path
from .views import TaskListApiView, TaskDeleteApiView
app_name = 'task-api'
urlpatterns = [
    path('', TaskListApiView.as_view(), name='list'),
    path('delete/<int:pk>', TaskDeleteApiView.as_view(), name='delete'),

]
