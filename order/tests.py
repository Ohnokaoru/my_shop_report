from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from userprofile.models import UserProfile

user = User.objects.get(username="yourusername")
try:
    profile = user.userprofile
    print(profile.tel)
except UserProfile.DoesNotExist:
    print("UserProfile 不存在")
