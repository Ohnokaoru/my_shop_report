from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "product_price",
        "product_stock",
        "sales_quantity",
        "product_img",
    )
    search_fields = ("product_name",)
    ordering = ("id",)


admin.site.register(Product, ProductAdmin)
