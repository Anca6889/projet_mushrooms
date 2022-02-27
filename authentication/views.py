#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module contains all the views necessary to run the autenthication
Note: The django authentication engine have been modified to allow a user to
login with is email OR with his username. This changes can be found in:
authentication/backend.py
"""

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.urls.base import reverse_lazy
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register(request):
    """This view manage the creation of an user account and allow him to
    login"""

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, "Votre compte a été crée avec succès !")
            user = form.save()
            login(
                request, user,
                backend="authentication.backend.AuthenticationBackend"
                )
            return redirect(reverse("register"))
        else:
            print(form.errors)
            for field in form.errors:
                print(field)

    context = {"form": form}
    return render(request, "register.html", context)


def sign_in(request):
    """This view allow an user to authenticate himself and login"""

    form = LoginForm()

    if request.method == "POST":
        email_or_user = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email_or_user, password=password)

        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return render(request, "home.html")
        else:
            messages.error(request, "L'email ou le mot de passe est incorrect")

    context = {"form": form}
    return render(request, "login.html", context)


@login_required()
def account(request):
    """This view return the user account page with his informations"""

    actual_user = request.user
    context = {"user": actual_user}
    return render(request, "account.html", context)


@login_required()
def sign_out(request):
    """This view logout the user"""

    logout(request)
    return render(request, "home.html")


class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, "password_success.html")


def password_reset_request(request):
    """Manage to reset user password"""

    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            messages.success(
                request, "Email de réinitialisation du mot de passe envoyé !"
            )
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "guth.jeanmaxime@gmail.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/password_reset")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
