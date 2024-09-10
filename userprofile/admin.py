from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "email", "tel", "address")
    search_fields = ("username", "email")
    list_filter = ("username",)
    ordering = ("id",)


admin.site.register(UserProfile, UserProfileAdmin)
