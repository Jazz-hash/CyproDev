from .serializers import PortfolioDisplaySerializer
from rest_framework import generics
from rest_framework import permissions
from portfolio.models import Portfolio
from services.models import Service
from rest_framework import filters
from django.db.models import Q


class PortfolioListApiView(generics.ListAPIView):
    serializer_class = PortfolioDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query:
            service = Service.objects.get(Q(head__iexact=query))
            portfolios = Portfolio.objects.filter(
                category=service).prefetch_related('porfolio_images')
        else:
            portfolios = Portfolio.objects.all().prefetch_related('porfolio_images')
        return portfolios
