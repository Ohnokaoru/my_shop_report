from django.urls import path
from . import views

urlpatterns = [
    path("confirm-order/", views.confirm_order, name="confirm-order"),
    path("review-order/", views.review_order, name="review-order"),
    path(
        "review-order-detail/<int:order_id>/",
        views.review_order_detail,
        name="review-order-detail",
    ),
    path(
        "sales-quantity-barchart/",
        views.sales_quantity_barchart,
        name="sales-quantity-barchart",
    ),
]
