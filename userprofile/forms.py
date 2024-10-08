from django import forms
from .models import UserProfile


class UserprofileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        exclude = ("user",)
