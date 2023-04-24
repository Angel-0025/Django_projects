from django.db import models
from django.utils import timezone


class Blog_User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=150)
    author = models.ForeignKey(Blog_User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title

