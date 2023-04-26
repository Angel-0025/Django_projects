from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title

