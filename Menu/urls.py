from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'lista'
urlpatterns = [
    path('', category),
    path('product/', product, name='product'),
    path('make_pr/', ProductView.as_view(), name='make_pr'),
    path('pro/', ProductList.as_view(), name='pro'),
    path('make/', ProductView.as_view(), name='make'),
]