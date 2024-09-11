from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from product.models import Product
from django.contrib import messages

# Create your views here.


# 新增購物車
def add_cart(request, product_id):
    message = ""
    # 抓product資料
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        form = CartItemForm(request.POST)

        if form.is_valid():
            # 抓取欄位
            quantity = form.cleaned_data("quantity")
            if product.product_stock < quantity:
                message = f"庫存不足，最大庫存量為{product.product_stock}"
            else:
                cartitemform = form.save(commit=False)
                cartitemform.product = product
                cartitemform.user = request.user
                cartitemform.save()
                message = "商品已成功加入購物車"

                # 更新庫存(因product為某一商品的實體物件，擁有該實體物件的所有內容，並可以做運算)
                product.product_stock -= quantity
                product.save()

        else:
            message = "資料錯誤"

    else:
        form = CartItemForm()

    return redirect("review-product")
