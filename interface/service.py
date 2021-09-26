"""
    This module contains all the basic methods of app/views.py
    This way alow a optimise refactoring and make it easier to unittest.
"""

from interface.models import Mushroom
from django.db.models import Count
from django.db.models import Q

class Service:
    """Contain all the methods of interface views."""

    def get_all_mushrooms(self):
        """get all the mushrooms ONLY with pictures"""

        return Mushroom.objects.filter(image__isnull=False).order_by("espece")
    
    def set_mushrooms_context(self, mushrooms):
        """setup atoz context"""

        context = {
            "mushrooms": mushrooms
        }
        return context

    def get_mushroom(self, mushroom_id):
        """get a simple mushroom with his id"""

        return Mushroom.objects.get(pk=mushroom_id)

    def search_results_with_name(self, query):
        """get results with research in search bar"""

        return Mushroom.objects.filter(image__isnull=False).filter(
            Q(espece__icontains=query) | Q(nom_vernaculaire__icontains=query)
        ).order_by("espece")

    def sort_by_edible_very_good(self):

        return Mushroom.objects.filter(image__isnull=False).filter(comestibilite__exact="bon comestible").order_by("espece")
    
    def sort_by_edible_good(self):

        return Mushroom.objects.filter(image__isnull=False).filter(comestibilite__exact="comestible").order_by("espece")

    def sort_by_edible_deadly(self):

        return Mushroom.objects.filter(image__isnull=False).filter(comestibilite__exact="mortel").order_by("espece")

    def sort_by_edible_toxic(self):

        return Mushroom.objects.filter(image__isnull=False).filter(comestibilite__exact="toxique").order_by("espece")
