from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserprofileForm
from .models import UserProfile

# Create your views here.


# 新增基本資料
@login_required
def create_userprofile(request):
    try:
        UserProfile.objects.get(user=request.user)
        return redirect("chalogin")

    except UserProfile.DoesNotExist:
        message = ""
        userprofileform = None
        if request.method == "POST":
            form = UserprofileForm(request.POST)

            if form.is_valid():
                userprofileform = form.save(commit=False)
                userprofileform.user = request.user
                userprofileform.save()
                message = "基本資料新增完成"

            else:
                message = "資料錯誤"

        else:
            form = UserprofileForm()

        return render(
            request,
            "userprofile/create-userprofile.html",
            {"form": form, "message": message, "userprofileform": userprofileform},
        )


# 瀏覽基本資料
@login_required
def review_userprofile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect("create-userprofile")

    return render(
        request, "userprofile/review-userprofile.html", {"userprofile": userprofile}
    )
