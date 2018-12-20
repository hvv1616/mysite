from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

# Create your models here.


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistratinoForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    # 检查两次密码是否相符
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']



    # 检查用户名
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("用户名太短")
        elif len(username) > 50:
            raise forms.ValidationError("用户名太长")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("用户名已存在")
            else:
                return username


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("phone", "birth")