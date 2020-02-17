from rest_framework import serializers
from portfolio.models import Portfolio, Image
from accounts.api.serializers import UserDisplaySerializer


class PortfolioImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class PortfolioDisplaySerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    porfolio_images = PortfolioImagesSerializer(
        many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'user', 'name', 'description', 'category', 'porfolio_images'
        ]
