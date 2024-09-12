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
        return redirect("review-product")

    return render(
        request,
        "cart/review-cart.html",
        {"cartitems": cartitems, "total_amount": total_amount},
    )


# 修改購物車
@login_required
def edit_cartitem(request, product_id):
    message = ""
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect("review-product")
    try:
        cartitem = CartItem.objects.get(user=request.user, product=product)

    except CartItem.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        form = CartItemForm(request.POST, instance=cartitem)

        if form.is_valid():
            quantity = form.cleaned_data.get("quantity")
            if quantity > cartitem.product.product_stock:
                message = f"目前庫存量:{cartitem.product.product_stock}，你的商品數量大於庫存，請設定有效商品數量"

            elif quantity == 0:
                cartitem.delete()
                return redirect("review-cart")

            else:
                cartitemform = form.save(commit=False)
                cartitemform.user = request.user
                cartitemform.product = product

                cartitemform.save()
                message = "更新成功"

    else:
        form = CartItemForm(instance=cartitem)

    return render(
        request,
        "cart/edit-cartitem.html",
        {"cartitem": cartitem, "form": form, "message": message},
    )


# 刪除購物車項目
@login_required
def delete_cartitem(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect("review-cart")

    try:
        cartitem = CartItem.objects.get(user=request.user, product=product)
    except CartItem.DoesNotExist:
        return redirect("review-cart")

    cartitem.delete()
    return redirect("review-cart")
