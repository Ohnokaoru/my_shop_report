from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
# 訂單資訊
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=50)
    total_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} {self.shipping_address}"


# 轉移購物車內容到此，商品詳細內容
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"商品:{self.product.product_name} 數量:{self.quantity} 下單時商品價格:{self.order_price} "
