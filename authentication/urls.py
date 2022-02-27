#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module contain all the necessary urls of the authentication
"""

from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.sign_in, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
    path(
        "password_reset/",
        views.password_reset_request,
        name="password_reset"
        ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password/",
        views.PasswordsChangeView.as_view(
            template_name="change_password.html"
            ),
        name="change_password",
    ),
    path("password_success", views.password_success, name="password_success"),
    path("logout", views.sign_out, name="logout"),
]
