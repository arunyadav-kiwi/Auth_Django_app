from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('New User created sucessfully'))
            return redirect('index')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})


def index(request):
    return render(request, 'index.html')