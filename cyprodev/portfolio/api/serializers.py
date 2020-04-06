from rest_framework import serializers
from portfolio.models import Portfolio, Image
from services.models import Service
from accounts.api.serializers import UserDisplaySerializer


class PortfolioImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class CategoryDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['head']


class PortfolioDisplaySerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    porfolio_images = PortfolioImagesSerializer(
        many=True, read_only=True)
    category = CategoryDisplaySerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'id', 'user', 'name', 'description', 'category', 'porfolio_images'
        ]
