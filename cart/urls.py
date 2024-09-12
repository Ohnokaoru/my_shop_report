from django.urls import path
from . import views

urlpatterns = [
    path("review-cart/", views.review_cart, name="review-cart"),
    path("edit-cart/<int:product_id>", views.edit_cart, name="edit-cart"),
]
