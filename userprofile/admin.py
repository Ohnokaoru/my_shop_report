from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "email", "tel", "address")
    search_fields = ("user__username", "email")
    list_filter = ("user__username",)
    ordering = ("id",)

    # obj為實體物件
    def username(self, obj):
        return obj.user.username


admin.site.register(UserProfile, UserProfileAdmin)
