from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "order_time", "shipping_address", "status")
    list_filter = ("id", "status")
    ordering = ("-order_time",)

    def username(self, obj):
        return obj.user.username


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "quantity", "order_price")
    ordering = ("-id",)

    def product_name(self, obj):
        return obj.product.product_name


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
