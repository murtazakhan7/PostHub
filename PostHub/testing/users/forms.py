from .models import UserModel
# from django.db import models
from django import forms

class UserPost(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['name','email','password']