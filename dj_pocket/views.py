# from django.shortcuts import render

# def home(requests):
#     return render(requests, "home.html")
from django.views.generic import TemplateView

class Homeview(TemplateView):
    template_name = 'home.html'