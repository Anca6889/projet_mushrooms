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

    def set_final_engine_context(self, color_top, form, color_under, ring, final_results):

        context = {
            "color_top": color_top,
            "form": form,
            "color_under": color_under,
            "ring": ring,
            "mushrooms": final_results
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

###############################################################################

#################### METHODS OF SORTING OUT BY EDIBILITY ####################

    def sort_by_edible_very_good(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="bon comestible").order_by("espece")

    def sort_by_edible_good(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="comestible").order_by("espece")

    def sort_by_edible_bad_good(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="mauvais comestible").order_by("espece")

    def sort_by_edible_bad(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="non comestible").order_by("espece")

    def sort_by_edible_deadly(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="mortel").order_by("espece")

    def sort_by_edible_toxic(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                comestibilite__exact="toxique").order_by("espece")

###############################################################################

############# METHODS OF 1st QUESTION OF ENGINE SORT BY COLOR_TOP #############

    def sort_by_color_top_red(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                couleur_du_chapeau__icontains="rouge").order_by("espece")

    def sort_by_color_top_white(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                Q(couleur_du_chapeau__icontains="blanc") | Q(
                    couleur_du_chapeau__icontains="creme") | Q(
                    couleur_du_chapeau__icontains="gris")).order_by("espece")

    def sort_by_color_top_yellow(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                Q(couleur_du_chapeau__icontains="jaune") | Q(
                    couleur_du_chapeau__icontains="orange")).order_by("espece")

    def sort_by_color_top_brown(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                Q(couleur_du_chapeau__icontains="brun") | Q(
                    couleur_du_chapeau__icontains="noir")).order_by("espece")

    def sort_by_color_top_other(self):

        return Mushroom.objects.filter(
            image__isnull=False).filter(
                Q(couleur_du_chapeau__icontains="violet") | Q(
                    couleur_du_chapeau__icontains="bleu") | Q(
                    couleur_du_chapeau__icontains="rose") | Q(
                    couleur_du_chapeau__icontains="vert")).order_by("espece")

###############################################################################

############### METHODS OF 2nd QUESTION OF ENGINE SORT BY FORM ###############

    def sort_by_lamelles(self, first_sort):

        return Mushroom.objects.filter(
            pk__in=first_sort).filter(dessous_du_chapeau="lamelles").order_by("espece")

    def sort_by_tubes(self, first_sort):

        return Mushroom.objects.filter(
            pk__in=first_sort).filter(dessous_du_chapeau="tubes").order_by("espece")

    def sort_by_plis(self, first_sort):

        return Mushroom.objects.filter(
            pk__in=first_sort).filter(dessous_du_chapeau="plis fourchus").order_by("espece")

    def sort_by_aiguillons(self, first_sort):

        return Mushroom.objects.filter(
            pk__in=first_sort).filter(dessous_du_chapeau="aiguillons").order_by("espece")

    def sort_by_no_lamelles_and_tubes(self, first_sort):

        return Mushroom.objects.filter(
            pk__in=first_sort).filter(dessous_du_chapeau="ni lamelles ni tubes").order_by("espece")

###############################################################################

############ METHODS OF 3rd QUESTION OF ENGINE SORT BY COLOR UNDER ############

    def sort_by_color_under_white(self, second_sort):

        return Mushroom.objects.filter(
            pk__in=second_sort).filter(
                Q(couleur_au_dessous_du_chapeau__icontains="blanc") | Q(
                    couleur_au_dessous_du_chapeau__icontains="creme") | Q(
                    couleur_au_dessous_du_chapeau__icontains="gris")).order_by("espece")

    def sort_by_color_under_brown(self, second_sort):

        return Mushroom.objects.filter(
            pk__in=second_sort).filter(
                Q(couleur_au_dessous_du_chapeau__icontains="brun") | Q(
                    couleur_au_dessous_du_chapeau__icontains="noir")).order_by("espece")

    def sort_by_color_under_yellow(self, second_sort):

        return Mushroom.objects.filter(
            pk__in=second_sort).filter(
                Q(couleur_au_dessous_du_chapeau__icontains="jaune") | Q(
                    couleur_au_dessous_du_chapeau__icontains="orange") | Q(
                    couleur_au_dessous_du_chapeau__icontains="ocre")).order_by("espece")

    def sort_by_color_under_red(self, second_sort):

        return Mushroom.objects.filter(
            pk__in=second_sort).filter(
                couleur_au_dessous_du_chapeau__icontains="rouge").order_by("espece")

    def sort_by_color_under_other(self, second_sort):

        return Mushroom.objects.filter(
            pk__in=second_sort).filter(
                Q(couleur_au_dessous_du_chapeau__icontains="rose") | Q(
                    couleur_au_dessous_du_chapeau__icontains="bleu") | Q(
                    couleur_au_dessous_du_chapeau__icontains="violet") | Q(
                    couleur_au_dessous_du_chapeau__icontains="vert") | Q(
                    couleur_au_dessous_du_chapeau__icontains="rouille")).order_by("espece")

###############################################################################

############## METHODS OF 4th QUESTION OF ENGINE SORT BY RING ################

    def sort_by_ring(self, third_sort):

        return Mushroom.objects.filter(
            pk__in=third_sort).filter(presence_d_un_anneau__exact="oui").order_by("espece")

    def sort_by_not_ring(self, third_sort):

        return Mushroom.objects.filter(
            pk__in=third_sort).filter(presence_d_un_anneau__exact="non").order_by("espece")

###############################################################################

############################# FAVORITES METHOD ###############################

    def add_or_remove_favorite(self, mushroom, user):
        """Add or remove a mushroom in favorites list by clicking on heart"""

        if mushroom.favorites.filter(id=user.id).exists():
            mushroom.favorites.remove(user.id)
        else:
            mushroom.favorites.add(user.id)

    def setup_favorites_list_context(self, favorites):
        """Setup the context of the view favorites_list in views.py"""

        context = {"favorites": favorites}
        return context

    def sort_out_user_favorite_mushrooms(self, mushrooms, user):
        """
        check if a product in list of mushrooms is already
        in user's favorites list
        """
        for mushroom in mushrooms:
            if mushroom.favorites.filter(id=user.id).exists():
                mushroom.is_fav = True
            else:
                mushroom.is_fav = False
        return mushrooms

    def sort_out_if_mushroom_is_favorite(self, mushroom, user):
        """check if a single mushroom is already in user's favorites list"""

        if mushroom.favorites.filter(id=user.id).exists():
            mushroom.is_fav = True
        else:
            mushroom.is_fav = False
        return mushroom
