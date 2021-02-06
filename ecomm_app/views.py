from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def women(request):
    return render(request, 'women.html')

def men(request):
    return render(request, 'men.html')

def accessories(request):
    return render(request, 'accessories.html')

def orders(request):
    return render(request, 'orders.html')

def account(request):
    return render(request, 'account.html')