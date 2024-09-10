from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# 註冊
def user_register(request):
    message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            message = "註冊成功"

        else:
            message = "資料錯誤:"

    else:
        form = UserCreationForm()

    return render(
        request, "user/user-register.html", {"message": message, "form": form}
    )
