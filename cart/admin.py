from django.contrib import admin
from django.contrib.auth.models import User
from product.models import Product
from .models import CartItem

# Register your models here.


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "product_name", "quantity")
    # 搜尋外鍵關聯欄位要加 "__"
    search_fields = ("user__username", "product__product_name")
    ordering = ("-id",)

    # self->CartItemAdmin，obj->CartItem
    def username(self, obj):
        return obj.User.username

    def product_name(self, obj):
        return obj.Product.product_name


admin.site.register(CartItem, CartItemAdmin)
