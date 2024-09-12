from django.shortcuts import render, redirect
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderForm

# Create your views here.


# 建立訂單資訊(order與商品細項的OrderItem)，最後清空購車
@login_required
def confirm_order(request):
    message = ""
    orderform = None

    cartitems = CartItem.objects.filter(user=request.user)

    # 計算總金額
    total_amount = 0
    for cartitem in cartitems:
        total_amount += cartitem.quantity * cartitem.product.product_price

    if not cartitems:
        return redirect("review-product")

    # 單筆Order會含多筆orderitem
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            orderform = form.save(commit=False)
            orderform.user = request.user
            orderform.total_amount = total_amount
            orderform.save()

            for cartitem in cartitems:
                # 手動驗證建立表單
                OrderItem.objects.create(
                    order=orderform,
                    product=cartitem.product,
                    quantity=cartitem.quantity,
                    order_price=cartitem.product.product_price,
                )

                # 更新庫存&更新銷售量
                cartitem.product.product_stock -= cartitem.quantity
                cartitem.product.sales_quantity += cartitem.quantity
                cartitem.product.save()

            message = "建立完成"

            # 清空購物車
            cartitems.delete()
            return redirect("review-product")

        else:
            message = "資料錯誤"

    else:
        form = OrderForm()

    return render(
        request,
        "order/confirm-order.html",
        {
            "cartitems": cartitems,
            "message": message,
            "form": form,
            "total_amount": total_amount,
        },
    )


# 查看訂單
@login_required
def review_order(request):
    message = ""
    orders = Order.objects.filter(user=request.user).order_by("-order_time")
    if not orders:
        message = "沒有下單紀錄"

    for order in orders:
        orderitems = OrderItem.objects.filter(order=order)

    return render(
        request,
        "order/review-order.html",
        {
            "message": message,
            "orders": orders,
            "orderitems": orderitems,
        },
    )
