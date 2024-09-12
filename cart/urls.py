from django.urls import path
from . import views

urlpatterns = [
    path("review-cart/", views.review_cart, name="review-cart"),
    path("edit-cartitem/<int:product_id>/", views.edit_cartitem, name="edit-cartitem"),
    path(
        "delete-cartcartitem/<int:product_id>/",
        views.delete_cartitem,
        name="delete-cartitem",
    ),
    path("clear-cartitem/", views.clear_cartitem, name="clear-cartitem"),
]
