from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth

urlpatterns = [
    path('',views.home, name='home'),
    path('viewproduct',views.viewproduct, name='viewproduct'),
    path('register/',views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
