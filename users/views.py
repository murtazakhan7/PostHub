from django.shortcuts import render,redirect
# from .forms import UserPost
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout 

from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request,user)
            return redirect(reverse('posts:index'))
    else:
           form=UserCreationForm()
     
    return render(request, 'users/index.html',{
            'form':form
        })
    
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            user=form.get_user()
            login(request,user)
            return redirect('posts:index')
    else:
        form=AuthenticationForm()
    return render(request,'users/login.html',{
        'form':form
    })

def logout(request):
    if request.method=='POST': 
        logout(request)
        return redirect('users/login')