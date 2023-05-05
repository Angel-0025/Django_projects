from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ToDoList, DoList
from .forms import ToDoListForm, DoListForm

@login_required()
def todolist_view(request):
    user = User.objects.get(id = request.user.id)
    todolist = ToDoList.objects.filter(user = request.user.id)
    
    context = {
            'list':todolist,
            'user':user
            }
    return render(request, 'todolist/todo_list_view.html', context)

def todolist_create(request):
    
    if request.method == 'POST':
        form = ToDoListForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            
            form.save()
            messages.success(request, f"Your blog is posted!.")
            return redirect('todolist-view')
            
    form = ToDoListForm()
    context = {
        'form':form 
    }
    return render(request, 'todolist/todo_list_create.html', context)

def dolist_view(request, pk):

    dolist = DoList.objects.filter(id = pk)
    
    todolist_id = ToDoList.objects.get(id = pk)
    
    context = {'list': dolist, 'todolist_id':todolist_id }
    return render(request, 'todolist/dolist_view.html', context)

def dolist_create(request, pk):
    
    todolist_id = ToDoList.objects.get(title = pk)
    
    form = DoListForm(initial={'todo_list': todolist_id })
    context = {'form': form}
    
    return render(request, 'todolist/dolist_create.html', context)