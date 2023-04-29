from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DoList(models.Model):
    topic = models.TextField(max_length=50)
    content = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.topic
    
