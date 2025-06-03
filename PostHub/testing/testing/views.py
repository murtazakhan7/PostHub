from django.shortcuts import render
from django.http import HttpResponse

def home(reuqest):
    return render(reuqest,'home.html')