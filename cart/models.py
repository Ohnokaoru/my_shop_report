from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} 商品:{self.product.product_name} 數量:{self.quantity}"
