from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, RegistratinoForm, UserProfileForm

# Create your views here.


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
            return render(request, "user_register/register.html", {"form": user_form})
    else:
        user_form = RegistratinoForm()
        userprofile_form = UserProfileForm()
        return render(request, "user_register/register.html", {"form": user_form, "profile": userprofile_form})
