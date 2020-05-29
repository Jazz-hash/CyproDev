from rest_framework import serializers
from tasks.models import Task
from services.models import Service
from accounts.api.serializers import UserDisplaySerializer


class TaskDisplaySerializer(serializers.ModelSerializer):
    assigned_to = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['assigned_to', 'task', 'description']
