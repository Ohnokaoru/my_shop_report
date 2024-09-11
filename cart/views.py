from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from product.models import Product

# Create your views here.


# 新增購物車
def add_cart(request, product_id):
    message - ""
    # 抓product資料
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        form = CartItemForm(request.POST)

        if form.is_valid():
            cartitemform = form.save(commit=False)
            cartitemform.product = product
            cartitemform.user = request.user
            cartitemform.save()
            message = "新增成功"

        else:
            message = "資料錯誤"

    else:
        form = CartItemForm()

    return render(request, "cart/add-cart.html", {"form": form, "message": message})
