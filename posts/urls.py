from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('newpost',views.newpost,name='newpost'),
    path('<slug:slug>',views.posts,name='list')
   
]
