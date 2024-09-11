from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meata:
        # 使用者與同一種商品只會出現一次實體物件(之後出現同一商品會並在同一筆)
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username} 商品:{self.product.product_name} 數量:{self.quantity}"
