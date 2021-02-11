from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('accessories/', views.accessories, name='accessories'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('account/', views.account, name='account'),
    path("accounts/signup", views.signup, name='signup'),
    path("account/edit_profile/", views.edit_profile, name='edit_profile'),
    path('orders/add_orderitem/<int:orderitem_id>/', views.add_orderitem, name='add_orderitem'),
    path('orders/delete_orderitem/<int:orderitem_id>/', views.delete_orderitem, name='delete_orderitem'),
]
