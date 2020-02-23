from django.urls import path
from .views import TaskListApiView
app_name = 'task-api'
urlpatterns = [
    path('', TaskListApiView.as_view(), name='list'),

]
