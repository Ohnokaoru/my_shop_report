from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
# 新增商品
def create_product(request):
    message = ""
    if request.method == "POST":
        # 需上傳檔案
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            productform = form.save(commit=False)
            productform.sales_quantity = 0
            productform.save()
            message = "新增成功"

        else:
            message = "資料錯誤"

    else:
        form = ProductForm()

    return render(
        request, "product/create-product.html", {"form": form, "message": message}
    )
