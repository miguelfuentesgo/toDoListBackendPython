from rest_framework import serializers
from .models import Task

def TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'done']