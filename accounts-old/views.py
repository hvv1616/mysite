from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth import authenticate,login
from .forms import LoginForm, RegistratinoForm, UserProfileForm

# Create your views here.

'''
def user_login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd =login_form.cleaned_data
            user=authenticate(username=cd['username'], password=cd ['password'])

            if user:
                login(request, user)
                return HttpResponse("Wellcome!")
            else:
                return HttpResponse("用户名或密码不正确！")
        else:
            return HttpResponse("Invalid login")

    if request.method=="GET":
        login_form=LoginForm()
        return render(request, "accounts/login.html", {"form": login_form})
'''


def register(request):
    if request.method == "POST":
        user_form = RegistratinoForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request, "registration/login.html", {"form": user_form})
        else:
            return render(request, "accounts/register.html", {"form": user_form})
    else:
        user_form = RegistratinoForm()
        userprofile_form = UserProfileForm()
        return render(request, "accounts/register.html", {"form": user_form, "profile": userprofile_form})
