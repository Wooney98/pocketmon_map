from django.shortcuts import render
from pbook.models import Pocket
from django.views.generic import ListView
# Create your views here.

# def index(requests):
#     pockets = Pocket.objects.all().order_by("name")
#     return render(requests, "index.html",{"pockets":pockets})

class index(ListView):
    model = Pocket
    template_name = 'pocket_list.html'
    paginate_by = 68 # pagination 기능, page 당 3개
    ordering = 'name'