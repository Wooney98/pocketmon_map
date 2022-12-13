from django.contrib import admin
from django.urls import path
#from pbook.views import index
from . import views

app_name = 'pbook'
urlpatterns = [
    #path('',loading, name = "loading"),
    path('list/',views.index.as_view(), name = "pocket_list"),  

]