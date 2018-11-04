from django.contrib import admin
from django.conf.urls import url
from . import views                #import views from the current directory

urlpatterns = [
    url(r'^',views.index,name='index'),       #r stands for raw String, ^ is starting and $ is ending
]                                               #view.index means to call index() function from views.py
                                    



