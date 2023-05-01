from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DoList
from .forms import DoListForm

# Create your views here.
@login_required(login_url="/login/")
def toDoList(request):
    
    user = User.objects.get(id = request.user.id)
    list = DoList.objects.filter(user = user.id)
    
    return render(request, 'todolist/list_display.html', {'list':list})

def toDoList_view(request, pk):
    list = DoList.objects.get(id = pk)

    return render(request, 'todolist/list_view.html', {'list':list})
    
def toDoList_create(request):
    if request.method == "POST":
        form = DoListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user

            form.save()
            messages.success(request, f"Your blog is posted!.")
            return redirect('todolist-view')
        
    form = DoListForm()
    
    return render(request, 'todolist/list_create.html', {'form':form})

def toDoList_update(request, pk):
    list = DoList.objects.get(id = pk)
    
    if request.method == 'POST':
        form = DoListForm(request.POST, instance = list)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your To-do list is updated!.")
            return redirect('todolist-view', pk=list.id)
    list = DoList.objects.get(id = pk)
    
    form = DoListForm(instance=list)
    
    return render(request, 'todolist/list_update.html', {'form':form})

def toDoList_delete(request, pk):
    list = DoList.objects.get(id = pk)
    
    if request.method == 'POST':
        list.delete()
        messages.success(request, f"Your to-do list is deleted!.")
        return redirect('todolist')
    
    return render(request, 'todolist/list_delete.html', {'list': list})