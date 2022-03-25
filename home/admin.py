from distutils.sysconfig import customize_compiler
from itertools import product
from unicodedata import category
from django.contrib import admin
from .models import Customer, Category, Order,Product, Cart, CartProduct
# Register your models here.

admin.site.register([Customer, Category,Product, Cart, CartProduct,Order ])