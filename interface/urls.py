"""
This module contain all the necessary urls of the base and product research
"""

from django.urls import path
from interface import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info', views.info, name="info"),
    path('atoz', views.atoz, name="atoz"),
    path("explore/", views.SearchResults.as_view(), name="search_list"),
    path("mushroom/<int:mushroom_id>/", views.mushroom_details, name="mushroom"),
    path("sort_by_edible_very_good/", views.sort_by_edible_very_good,
         name="sort_by_edible_very_good"),
    path("sort_by_edible_good/", views.sort_by_edible_good,
             name="sort_by_edible_good"),
    path("sort_by_edible_bad_good/", views.sort_by_edible_bad_good,
         name="sort_by_edible_bad_good"),
    path("sort_by_edible_bad/", views.sort_by_edible_bad,
         name="sort_by_edible_bad"),
    path("sort_by_edible_toxic/", views.sort_by_edible_toxic,
         name="sort_by_edible_toxic"),
    path("sort_by_edible_deadly/", views.sort_by_edible_deadly,
         name="sort_by_edible_deadly"),
    path("engine2/<str:color_top>/", views.engine2,
         name="engine2"),
    path("engine3/<str:color_top>/<str:form>/", views.engine3,
         name="engine3"),
    path("engine4/<str:color_top>/<str:form>/<str:color_under>/", views.engine4,
         name="engine4"),
    path("engine_results/<str:color_top>/<str:form>/<str:color_under>/<str:ring>/", views.engine_results,
         name="engine_results"),
    path("add_or_remove_favorite/<int:mushroom_id>/",
         views.add_or_remove_favorite, name="add_or_remove_favorite"),
    path("favorites/", views.favorites_list, name="favorites")
]   
