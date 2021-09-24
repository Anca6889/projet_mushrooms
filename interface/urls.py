"""
This module contain all the necessary urls of the base and product research
"""

from django.urls import path
from interface import views

urlpatterns = [
    path('', views.index, name="index"),
    path('atoz', views.atoz, name="atoz"),
    path("explore/", views.SearchResults.as_view(), name="search_list"),
    
]
