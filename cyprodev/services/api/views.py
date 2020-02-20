from .serializers import ServiceDisplaySerializer
from rest_framework import generics
from rest_framework import permissions
from services.models import Service
from rest_framework import filters


class ServiceListApiView(generics.ListAPIView):
    serializer_class = ServiceDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
