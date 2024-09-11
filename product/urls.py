from django.urls import path
from . import views

urlpatterns = [
    path("create-product/", views.create_product, name="create-product"),
    path("review-product/", views.review_product, name="review-product"),
    path("", views.review_product, name="review-product"),
    path(
        "review-product-detail/<int:product_id>/",
        views.review_product_detail,
        name="review-product-detail",
    ),
    path(
        "edit-product/<int:product_id>/",
        views.edit_product,
        name="edit-product",
    ),
    path(
        "delete-product/<int:product_id>", views.delete_product, name="delete-product"
    ),
]
