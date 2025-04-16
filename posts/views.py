from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def index(request):
    # return HttpResponse("Welocme to my posts")
    Posts=Post.objects.all()
    return render(request,'posts/post.html',{
        'posts':Posts
    })

def posts(request,slug):
    Posts=Post.objects.get(slug=slug)
    return render(request,'posts/list.html',{
        'post':Posts
    })

@login_required(login_url='/users:login')
def newpost(request):
    if request.method=='POST':
        form = forms.NewPost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return redirect('posts:list')
        
        return redirect('posts:index')
    else:
        form = forms.NewPost()
    return render(request,'posts/newpost.html',{
        'form':form
    })