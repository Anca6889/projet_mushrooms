"""
This module contain all the necessary urls of the authentication
"""

from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.sign_in, name="login"),
    path('register/', views.register, name="register"),
    path("account/", views.account, name="account"),
    path("logout", views.sign_out, name="logout"),
]
