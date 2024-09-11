from django.urls import path
from . import views

urlpatterns = [
    path("add-cart/", views.add_cart, name="add-cart"),
]
