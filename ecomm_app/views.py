from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def women(request):
    return render(request, 'womens/women.html')

def men(request):
    return render(request, 'mens/men.html')

def accessories(request):
    return render(request, 'accessories/accessories.html')

def orders(request):
    return render(request, 'cart/orders.html')

def account(request):
    return render(request, 'users/account.html')
