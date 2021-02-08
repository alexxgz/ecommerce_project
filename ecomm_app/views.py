from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


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

def signup(request):
    error_message=""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
        else:
            error_message = 'Ivalid sign up - try again!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



def women(request):
    return render(request, 'womens/women.html')

def men(request):
    return render(request, 'mens/men.html')

def accessories(request):
    return render(request, 'accessories/accessories.html')

def orders(request):
    return render(request, 'cart/orders.html')

def account(request):
    return render(request, 'members/account.html')
