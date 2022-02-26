"""This module will test all the urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from interface.views import SearchResults
from interface import views


class UrlsTests(SimpleTestCase):
    """
    This class will test the urls using resolve and reverse modules
    Each method name describe exactly which url is tested.
    """

    def test_index_url_is_resolved(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, views.index)

    def test_info_url_is_resolved(self):
        url = reverse("info")
        self.assertEquals(resolve(url).func, views.info)

    def test_atoz_url_is_resolved(self):
        url = reverse("atoz")
        self.assertEquals(resolve(url).func, views.atoz)

    def test_explore_url_is_resolved(self):
        resolver = resolve(reverse("search_list"))
        self.assertEquals(resolver.func.__name__,
                          SearchResults.as_view().__name__)

    def test_mushroom_details_url_is_resolved(self):
        url = reverse("mushroom", kwargs={"mushroom_id": 1})
        self.assertEquals(resolve(url).func, views.mushroom_details)

    def test_sort_by_edible_very_good_url_is_resolved(self):
        url = reverse("sort_by_edible_very_good")
        self.assertEquals(resolve(url).func, views.sort_by_edible_very_good)

    def test_sort_by_edible_good_url_is_resolved(self):
        url = reverse("sort_by_edible_good")
        self.assertEquals(resolve(url).func, views.sort_by_edible_good)

    def test_sort_by_edible_bad_good_url_is_resolved(self):
        url = reverse("sort_by_edible_bad_good")
        self.assertEquals(resolve(url).func, views.sort_by_edible_bad_good)

    def test_sort_by_edible_bad_url_is_resolved(self):
        url = reverse("sort_by_edible_bad")
        self.assertEquals(resolve(url).func, views.sort_by_edible_bad)

    def test_sort_by_edible_toxic_url_is_resolved(self):
        url = reverse("sort_by_edible_toxic")
        self.assertEquals(resolve(url).func, views.sort_by_edible_toxic)

    def test_sort_by_edible_deadly_url_is_resolved(self):
        url = reverse("sort_by_edible_deadly")
        self.assertEquals(resolve(url).func, views.sort_by_edible_deadly)

    def test_engine2_url_is_resolved(self):
        url = reverse("engine2", kwargs={"color_top": "rouge"})
        self.assertEquals(resolve(url).func, views.engine2)

    def test_engine3_url_is_resolved(self):
        url = reverse("engine3", kwargs={
                      "color_top": "rouge", "form": "lamelles"})
        self.assertEquals(resolve(url).func, views.engine3)

    def test_engine4_url_is_resolved(self):
        url = reverse(
            "engine4",
            kwargs={"color_top": "rouge",
                    "form": "lamelles", "color_under": "blanc"},
        )
        self.assertEquals(resolve(url).func, views.engine4)

    def test_engine_results_url_is_resolved(self):
        url = reverse(
            "engine_results",
            kwargs={
                "color_top": "rouge",
                "form": "lamelles",
                "color_under": "blanc",
                "ring": "oui",
            },
        )
        self.assertEquals(resolve(url).func, views.engine_results)

    def test_add_or_remove_favorite_url_is_resolved(self):
        url = reverse("add_or_remove_favorite", kwargs={"mushroom_id": 1})
        self.assertEquals(resolve(url).func, views.add_or_remove_favorite)

    def test_favorites_url_is_resolved(self):
        url = reverse("favorites",)
        self.assertEquals(resolve(url).func, views.favorites_list)
