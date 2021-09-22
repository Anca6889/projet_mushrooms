"""
This module contain all the necessary urls of the base and product research
"""

from django.urls import path
from interface import views

urlpatterns = [
    path('', views.index, name="index"),
    
]
