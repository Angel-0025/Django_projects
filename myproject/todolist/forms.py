from django.forms import ModelForm
from .models import ToDoList, DoList

class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']
        
class DoListForm(ModelForm):
    class Meta:
        model = DoList
        fields = ['todo_list','title','description','date_created']