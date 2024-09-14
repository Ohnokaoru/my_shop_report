from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import chaloginForm
from django.contrib.auth.models import User

# Create your views here.


# 註冊
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("chalogin")

        else:
            message = "資料錯誤:"

    else:
        form = UserCreationForm()

    return render(
        request, "user/user-register.html", {"message": message, "form": form}
    )


# 登入
def chalogin(request):
    message = ""
    if request.method == "POST":
        form = chaloginForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("create-userprofile")

        else:
            message = "資料錯誤"

    else:
        form = chaloginForm()

    return render(request, "user/chalogin.html", {"form": form, "message": message})


# 登出
def user_logout(request):
    logout(request)
    return redirect("chalogin")
