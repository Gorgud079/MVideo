from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem

def index(request):
    menu = MenuItem.objects.all()
    return render(request, 'base.html', {'menu': menu})

def category(request):
    return HttpResponse('<h1>Категория</h1>')


def product(request):
    return HttpResponse('<h1>Продукты</h1>')
# Create your views here.
