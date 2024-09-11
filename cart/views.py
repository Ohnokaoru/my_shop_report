from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from product.models import Product
from django.contrib import messages

# Create your views here.


# 檢視購物車
# def review_cart(request):

#     CartItem.get
