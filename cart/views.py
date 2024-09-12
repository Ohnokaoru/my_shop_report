from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


# # 檢視購物車
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


# # 修改購物車
@login_required
def edit_cart(request, product_id):
    message = ""

    cartitem = CartItem.objects.get(user=request.user, product__id=product_id)

    if request.method == "POST":
        form = CartItemForm(request.POST, instance=cartitem)

        if form.is_valid():
            quantity = form.cleaned_data.get("quantity")
            if quantity > cartitem.product.product_stock:
                message = f"數量大於庫存，目前庫存量為:{cartitem.product.product_stock}"

            form.save()
            message = "更新成功"
    else:
        form = CartItemForm(instance=cartitem)

    return render(
        request,
        "cart/edit-cart.html",
        {"cartitems": cartitem, "form": form, "message": message},
    )
