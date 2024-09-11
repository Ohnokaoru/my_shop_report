from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
# 新增商品
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


# 瀏覽商品內容
def review_product_detail(request, product_id):
    message = ""
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect("review-product")

    return render(
        request,
        "product/review-product-detail.html",
        {"product": product, "message": message},
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
