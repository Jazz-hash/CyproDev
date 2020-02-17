from .serializers import PortfolioDisplaySerializer
from rest_framework import generics
from rest_framework import permissions
from portfolio.models import Portfolio


class PortfolioListApiView(generics.ListAPIView):
    serializer_class = PortfolioDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Portfolio.objects.all().prefetch_related('porfolio_images')
