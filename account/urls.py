from django import template
from pyrsistent import v
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]