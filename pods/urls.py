from django.conf.urls import url,include 
from django.urls import  path,re_path
from . import views
#1
from pods.views import  *
urlpatterns = [
    path("", views.index, name='index'),

    
    
]
