from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ToDoList, DoList
from .forms import ToDoListForm, DoListForm

# view the Todo list topics 
@login_required()
def todolist_view(request):
    user = User.objects.get(id = request.user.id)
    
    todolist = ToDoList.objects.filter(user = request.user.id)
    
    context = {
            'list':todolist,
            'user':user
            }
    return render(request, 'todolist/todo_list_view.html', context)

# Create the todo list topic
def todolist_create(request):
    
    if request.method == 'POST':
        form = ToDoListForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            
            form.save()
            messages.success(request, f"Your Todo list Topic is created!.")
            return redirect('todolist-view')
            
    form = ToDoListForm()
    context = {
        'form':form 
    }
    return render(request, 'todolist/todo_list_create.html', context)

# View the task inside the todolist topic
def dolist_view(request, pk):

    dolist = DoList.objects.filter(todo_list = pk)
    
    todolist_id = ToDoList.objects.get(id = pk)
    
    context = {'list':dolist, 'todolist_id':todolist_id }
    return render(request, 'todolist/dolist_view.html', context)

# Create/ add task to todolist topic
def dolist_create(request, pk):
    
    todolist_id = ToDoList.objects.get(title = pk)
    
    if request.method == 'POST':
        form = DoListForm(request.POST, initial={'todo_list': todolist_id })
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Todo list Task is added!.")
            return redirect('dolist-view', pk = todolist_id.id)
    
    
    form = DoListForm(initial={'todo_list': todolist_id })
    context = {'form': form}
    
    return render(request, 'todolist/dolist_create.html', context)


# to do 

# Delete in task view / this delete is for the topic
# Create the view, update, delete for specific task  