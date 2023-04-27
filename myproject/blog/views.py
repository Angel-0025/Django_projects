from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    context = {'post': Post.objects.all }
    return render(request, 'blog/home.html', context)

@login_required(login_url="/login/")
def newPost(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            
            form.save()
            messages.success(request, f"Your blog is posted!.")
            return redirect('index')
    
   
    form = PostForm()
    context = {'form':form}
    
    return render(request, 'blog/new_post.html', context)
             

def viewPost(request, pk):
    
    post = Post.objects.filter(id=pk)
    
    context = {'post':post}
    
    return render(request, 'blog/post_detail.html', context)

def editPost(request, pk):
    
    post = Post.objects.get(id = pk)
    
    if request.method == "POST":
        form = PostForm(instance=post, data = request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f"Your blog is updated!.")
            return redirect('view-post', pk=post.id)   
    
    form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

def deletePosted(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, f"Your blog is deleted!.")
        return redirect('index')
    
    return render(request, 'blog/post_delete.html', {'post': post})