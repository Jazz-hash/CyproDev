from .serializers import TaskDisplaySerializer
from rest_framework import generics
from rest_framework import permissions
from tasks.models import Task


class TaskListApiView(generics.ListAPIView):
    serializer_class = TaskDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.order_by('-created')[:5]


class TaskDeleteApiView(generics.DestroyAPIView):
    serializer_class = TaskDisplaySerializer
    queryset = Task.objects.all()
