from django.urls import path
from . import views

urlpatterns = [
    path("confirm-order/", views.confirm_order, name="confirm-order"),
    path("review-order/", views.review_order, name="review-order"),
]
