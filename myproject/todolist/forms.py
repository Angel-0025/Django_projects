from django.forms import ModelForm
from .models import ToDoList, DoList

class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        Fields = ['title']
        
class DoListForm(ModelForm):
    class Meta:
        model = DoList
        Fields = ['todo_list','title','description','date_created']