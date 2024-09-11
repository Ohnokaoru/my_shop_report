from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.PositiveIntegerField()
    # 設定圖片儲存路徑
    product_img = models.ImageField(upload_to="product_images/", null=True, blank=True)
    product_description = models.TextField(max_length=200)
    product_stock = models.PositiveIntegerField()
    sales_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} {self.product_stock} {self.sales_quantity}"
