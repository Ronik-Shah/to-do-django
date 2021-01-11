from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TaskSerilizer
from .models import Task
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerilizer
