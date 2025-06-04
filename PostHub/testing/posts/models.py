from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=100)
    body=models.TextField()
    time=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True)
    image=models.ImageField(blank=True)
    author = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
  
    
    def __str__(self) :
        return self.title
