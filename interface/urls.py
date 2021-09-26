"""
This module contain all the necessary urls of the base and product research
"""

from django.urls import path
from interface import views

urlpatterns = [
    path('', views.index, name="index"),
    path('atoz', views.atoz, name="atoz"),
    path("explore/", views.SearchResults.as_view(), name="search_list"),
    path("mushroom/<int:mushroom_id>/", views.mushroom_details, name="mushroom"),
    path("sort_by_edible_very_good/", views.sort_by_edible_very_good,
         name="sort_by_edible_very_good"),
    path("sort_by_edible_good/", views.sort_by_edible_good,
             name="sort_by_edible_good"),
    path("sort_by_edible_deadly/", views.sort_by_edible_deadly,
         name="sort_by_edible_deadly"),
    path("sort_by_edible_toxic/", views.sort_by_edible_toxic,
         name="sort_by_edible_toxic"),
]   
