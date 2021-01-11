from rest_framework import serializers

from .models import Task


class TaskSerilizer(serializers.ModelSerializer):
    createdAt = serializers.DateField(
        format="%d-%m-%y", input_formats=['%Y-%m-%d', 'iso-8601'])

    class Meta:
        model = Task
        fields = ('id', 'name', 'content', 'createdAt')
