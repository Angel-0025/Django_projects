from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    context = {'post': Post.objects.all }
    return render(request, 'blog/home.html', context)

def newPost(request):
    form = PostForm()
    
    return render(request, 'blog/new_post.html', {'form':form})