from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,blank=True)
    password = models.CharField(max_length=100)
    