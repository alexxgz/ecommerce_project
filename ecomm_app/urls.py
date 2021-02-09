from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('accessories/', views.accessories, name='accessories'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='orders'),
    path('account/', views.account, name='account'),
    path("accounts/signup", views.signup, name='signup'),

]
