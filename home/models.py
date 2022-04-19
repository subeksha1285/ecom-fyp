from distutils.command.upload import upload
from email.headerregistry import Address
from email.mime import image
from itertools import product
from msilib.schema import Class
from pickle import FALSE
from queue import Full
from turtle import title
from unicodedata import category
from venv import create
from django.contrib.auth.models import User
from django.db import models

# create your models here
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_list/")    
    price = models.PositiveIntegerField()
    description = models.TextField()
    return_policy = models.CharField(max_length=300, null=True, blank=True)   
    size = models. TextField(blank=True) 
    def __str__(self):
        return self.title

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True )
    total = models.PositiveIntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartProduct(models.Model):
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.Cart.id) + "CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed","Order Completed"),
    ("Order Cancelled", "Order Cancelled")
)
METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)

class Order(models.Model):
    Cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, blank=True)
    order_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=10)
    email = models.CharField(null=True, blank=True, max_length=50)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    
    def __str__(self):
        return "Ordes: " + str(self.id)