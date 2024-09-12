from django.contrib import admin


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "order_time", "shipping_address", "status")
    list_filter = ("id", "status")
    ordering = "-order_time"


class OrderItem(admin.ModelAdmin):
    list_display = ("id", "product_name", "quantity", "order_price")
    ordering = ("-id",)
