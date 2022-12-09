from django.contrib import admin
from django.urls import path
from pbook.views import index
from . import views

app_name = 'pbook'
urlpatterns = [
    #path('',loading, name = "loading"),
    path('',views.home,name = "home"),
    path('list/',index, name = "index"),
    path('list/post_list', views.post_list, name='post_list'),
]