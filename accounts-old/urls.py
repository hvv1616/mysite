"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="user_login"),
    path('logout/', auth_views.logout_then_login, name='user_logout'),
    path('register/', views.register, name="user_register"),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        success_url='/accounts/login'), name="password_change"),
    # path('password-reset/', auth_views.PasswordResetView.as_view(success_url='/accounts/password-reset-done'), name="password_reset"),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password-reset-confirm', auth_views.PasswordResetConfirmView.as_view(success_url='/accounts/password-reset-complete'), name="password_reset_confirm"),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
