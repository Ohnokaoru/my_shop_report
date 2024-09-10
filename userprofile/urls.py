from django.urls import path
from . import views

urlpatterns = [
    path("create-userprofile/", views.create_userprofile, name="create-userprofile"),
    path("review-userprofile/", views.review_userprofile, name="review-userprofile"),
]
