from django.urls import path
from . import views

urlpatterns = [
    path("create-product/", views.create_product, name="create-product"),
    path("review-product/", views.review_product, name="review-product"),
    path("", views.review_product, name="review-product"),
]
