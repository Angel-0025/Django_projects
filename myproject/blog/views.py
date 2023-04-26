from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    context = {'post': Post.objects.all }
    return render(request, 'blog/home.html', context)
             
"""
def viewPost(request, pk):
    
    post = Post.objects.filter(id=pk)
    context = {'post':post}
    
    return render(request, 'blog/post_detail.html', context)
    
def newPost(request):
    form = PostForm()
    
    if request.POST:
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save()
        
            return redirect('index')
    
    return render(request, 'blog/new_post.html', {'form':form})
        
"""