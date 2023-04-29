from django.forms import ModelForm
from .models import DoList

class DoListForm(ModelForm):
    class Meta:
        model = DoList
        fields = ['topic','content']