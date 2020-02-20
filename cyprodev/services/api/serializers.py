from rest_framework import serializers
from services.models import Service
from accounts.api.serializers import UserDisplaySerializer


class ServiceDisplaySerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Service
        fields = ['icon', 'head', 'description', 'user', 'created']
