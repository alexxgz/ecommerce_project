from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
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

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')    
    context = {}
    return render(request, 'registration/login.html', context)