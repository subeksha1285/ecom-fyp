from ast import Param
from math import ceil
from multiprocessing import context
from django.shortcuts import render, redirect
from home.models import Product
from .models import *
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def viewproduct(request):
    products = Product.objects.all()
    print(products)
    params = {'products' : products}
    return render(request, 'p1.html', params)

def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)                                                                                                                                                                                        