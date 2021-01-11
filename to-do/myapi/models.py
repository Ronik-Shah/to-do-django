from django.db import models
import datetime

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    createdAt = models.DateField()

    def __str__(self):
        return self.name
