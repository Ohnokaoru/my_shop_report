from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from cart.forms import CartItemForm
from cart.models import CartItem
from django.contrib.auth.decorators import login_required


# Create your views here.
# 新增商品
@staff_member_required
def create_product(request):
    message = ""
    if request.method == "POST":
        # 需上傳檔案
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            productform = form.save(commit=False)
            # 不需要顯式設置sales_quantity，default為 0
            # productform.sales_quantity = 0

            print(f"productform.product_img.path")
            productform.save()
            return redirect("review-product")

        else:
            message = "資料錯誤"

    else:
        form = ProductForm()

    return render(
        request, "product/create-product.html", {"form": form, "message": message}
    )


# 瀏覽商品(首頁)
def review_product(request):
    produsts = Product.objects.all().order_by("id")
    if not produsts:
        return redirect("create-product")

    paginator = Paginator(produsts, 4)
    try:
        page_number = int(request.GET.get("page", 1))

    except (ValueError, TypeError):
        page_number = 1

    page_obj = paginator.get_page(page_number)

    if request.user.is_staff:
        templates = "product/review-product-staff.html"
    else:
        templates = "product/review-product.html"

    return render(request, templates, {"page_obj": page_obj})


# 瀏覽商品內容&加入購物車
def review_product_detail(request, product_id):
    if not request.user.is_authenticated:
        return redirect("chalogin")

    message = ""
    # 抓取該商品資訊
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        # 只有數量可以填
        form = CartItemForm(request.POST)

        if form.is_valid():
            # 抓取欄數量欄位做庫存比較
            quantity = form.cleaned_data.get("quantity")

            if product.product_stock < quantity:
                message = f"庫存不足，最大庫存量為{product.product_stock}"

            else:
                try:
                    cartitem = CartItem.objects.get(user=request.user, product=product)
                    # 如果商品已經在購物車中，增加數量
                    cartitem.quantity += quantity
                    cartitem.save()
                    message = "已有同項商品了，幫你累加數量"

                # 如果商品不在購物車中，新增cartitem實體物件
                except CartItem.DoesNotExist:
                    cartitemform = form.save(commit=False)
                    cartitemform.product = product
                    cartitemform.user = request.user
                    cartitemform.save()
                    message = "商品已成功加入購物車"

        else:
            message = "資料錯誤"

    else:
        form = CartItemForm()

    return render(
        request,
        "product/review-product-detail.html",
        {"product": product, "message": message, "form": form},
    )


# 修改內容
@staff_member_required
def edit_product(request, product_id):
    message = ""
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            # 因為sales_quantity不是手動運算而是藉由訂單成立時增加的
            form.save()
            return redirect("review-product-detail", product_id=product_id)

        else:
            message = "資料錯誤"
    else:
        form = ProductForm(instance=product)

    return render(
        request, "product/edit-product.html", {"message": message, "form": form}
    )


# 刪除商品
@staff_member_required
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect("review-product")

    if request.method == "POST":
        product.delete()
        return redirect("review-product")

    return render(request, "product/delete-product.html", {"product": product})
