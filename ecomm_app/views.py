from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

from .forms import MemberForm, CheckoutForm, Item_Form, Order_Form
from .models import Account, Item, OrderItem, Order, Address, Payment, Coupon, Refund



def home(request):
    items = Item.objects.filter(discount_price=False)
    context = { 'items': items}
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def loginPage(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')  
        else:
            error_message = "Account not found"  
    context = {'error_message': error_message}
    return render(request, 'registration/login.html', context)


def signup(request):
    error_message=""
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            account = form.save()
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            city = request.POST.get('city')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirmPassword')
            return redirect('login')

        else:
            print(form.errors)
            error_message = 'Ivalid sign up - try again!'
    form = MemberForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def account(request):
    user=request.user
    if request.user.is_authenticated:
        context = {
            'user': user,
        }
        return render(request, 'members/account.html', context)
    else:
        return redirect('registration/signup.html')


def edit_profile(request):
    user=request.user
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=user)
        if form.is_valid():
            account = form.save()
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            city = request.POST.get('city')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirmPassword')            
            return redirect('login')

        else:
            print(form.errors)
    form = MemberForm(instance=user)
    context = {'form': form}
    return render(request, 'members/edit.html', context)  


def women(request):
    items = Item.objects.filter(department='W')
    context = { 'items': items}
    return render(request, 'womens/women.html', context)


def men(request):
    items = Item.objects.filter(department='M')
    context = { 'items': items}
    return render(request, 'mens/men.html', context)


def accessories(request):
    items = Item.objects.filter(department='A')
    context = { 'items': items}
    return render(request, 'accessories/accessories.html', context)


def orders(request):
    order_items = OrderItem.objects.all()
    total = 0
    total_items = 0
    for item in order_items:
        total += item.item.price * item.quantity
    for quantity in order_items:
        total_items += item.quantity
    context = { 
    'orderItems': order_items,
    'total': total,
    'total_items': total_items,
    }
    return render(request, 'cart/orders.html', context)


def add_orderitem(request, orderitem_id):
    added_item = OrderItem.objects.create(item_id=orderitem_id, user_id=request.user.id)
    added_item.save()
    return redirect('orders')


def delete_orderitem(request, orderitem_id):
    removed_from_cart = OrderItem.objects.get(id=orderitem_id).delete()
    return redirect('orders')


def checkout(request):
    return render(request, 'cart/checkout.html')

