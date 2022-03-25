from ast import Param
from math import ceil
from multiprocessing import context
from django.shortcuts import render
from home.models import Product
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def viewproduct(request):
    products = Product.objects.all()
    print(products)
    params = {'products' : products}
    return render(request, 'p1.html', params)

def log(request):
    return render(request, 'log.html')
                                                                                                                                                                                                                                                                   
