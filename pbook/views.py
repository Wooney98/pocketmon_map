from django.shortcuts import render
from pbook.models import Pocket

# Create your views here.
def index(requests):
    pockets = Pocket.objects.all().order_by("name")
    return render(requests, "index.html",{"pockets":pockets})