from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# 檢視購物車
@login_required
def review_cart(request):
    total_amount = 0

    cartitems = CartItem.objects.filter(user=request.user)
    for cartitem in cartitems:
        quantity = cartitem.quantity
        price = cartitem.product.product_price
        total_amount += quantity * price

        print(total_amount)

    if not cartitems:
        return redirect("review_product")

    return render(
        request,
        "cart/review-cart.html",
        {"cartitems": cartitems, "total_amount": total_amount},
    )
