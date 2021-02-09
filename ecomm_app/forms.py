from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Account, Item, OrderItem


class MemberForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'city', 'email')
        help_texts=""


class Item_Form(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price', 'discount_price', 'department','category', 'label', 'slug', 'description', 'image']

class Order_Form(ModelForm):       
    class Meta:
        model = OrderItem
        fields = ['ordered', 'item', 'quantity']


PAYMENT_CHOICES = (
    ('V', 'Visa'),
    ('P', 'PayPal')
)
class CheckoutForm(ModelForm):
    shipping_address = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

