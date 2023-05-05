from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class DoList(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    