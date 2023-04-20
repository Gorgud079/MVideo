from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormMixin
from .models import *
from django.views.generic.list import ListView
from django.views import View
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
load_dotenv()

def index(request):
    menu = MenuItem.objects.all()
    return render(request, 'base.html', {'menu': menu})

def category(request):
    return HttpResponse('<h1>Категория</h1>')


def product(request):
    return HttpResponse('<h1>Продукты</h1>')


class ProductList(ListView):
    model = Product
    template_name = 'base.html'
    context_object_name = 'pro'


class CategoryList(ListView):
    model = Category
    template_name = 'make_pr.html'
    context_object_name = 'category'


class ProductView(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        return render(request, 'make_pr.html', {'category': category})
    def post(self, request, *args, **kwargs):
        product = Product(
            name=request.POST['name_product'],
            description=request.POST['description_product']
        )
        product.save()
        product.categories.add(request.POST['categories'])
        send_mail(
            subject=f'Новый {product.name}',
            message=product.description,
            from_email=os.getenv("email_e"),
            recipient_list=['des079@inbox.ru']
        )
        return redirect('lista:product')

