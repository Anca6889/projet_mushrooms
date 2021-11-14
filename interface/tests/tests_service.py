"""This module will test all the methods in service.py used for the views"""

from django.test import TestCase
from django.contrib.auth.models import User
from interface.models import Mushroom
from interface.service import Service

service = Service()  # Load all the necessary methods from service.py


class ServiceTests(TestCase):
    """
    This class will use several mushroom mocks and 1 user mock
    to test all the service functions.
    """

    def setUp(self):
        """Setup the mocks and urls"""

        self.mock_user = User.objects.create(
            id='1',
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462'
        )

        self.mock_mushroom = Mushroom.objects.create(
            id='1',
            espece='amanita testa',
            diametre_minimum_du_chapeau='10',
            diametre_maximum_du_chapeau='15',
            couleur_du_chapeau='rouge',
            forme_du_chapeau='ovoide ',
            surface_du_chapeau='ecailleuse',
            type_de_marge='anodine',
            couleur_de_la_marge='neutre',
            dessous_du_chapeau='lamelles',
            couleur_au_dessous_du_chapeau='neutre',
            oxydation_du_chapeau='oxydation',
            couleur_de_l_oxydation_du_chapeau='bleu',
            mode_d_insertion_du_dessous_du_chapeau_avec_le_pied='libres',
            espace_entre_les_lamelles='serres',
            type_de_lamelles='normal',
            couleur_du_pied='neutre',
            pïed_creux_ou_plein='plein',
            forme_du_pied='pied long',
            surface_du_pied='rugeux',
            position_du_pied_par_rapport_au_chapeau='centrale',
            presence_d_un_anneau='oui',
            orientation_de_l_anneau='descendant',
            mobilite_de_l_anneau='non',
            couleur_de_l_anneau='neutre',
            poussee_en_touffe='non',
            couleur_de_la_base_du_pied='neutre',
            couleur_de_la_chair='neutre',
            oxydation_de_la_chair='oui',
            couleur_de_l_oxydation='bleu',
            fermete_de_la_chair='ferme',
            odeur='agreable',
            latex='oui',
            couleur_du_latex='neutre',
            mois_de_poussees_le_plus_tot='aout',
            mois_de_poussees_le_plus_tard='novembre',
            milieu='pres',
            pousse_sur_du_bois_ou_non='non',
            nom_vernaculaire='amanite test',
            comestibilite='toxique',
            commentaires='Ceci un commentaire test',
            synonymes='amanitas del testas',
            qq='qq test',
            image='testimage'
        )

        self.mock_white_toxic = Mushroom.objects.create(
            id='2',
            espece='amanita testa 2',
            diametre_minimum_du_chapeau='10',
            diametre_maximum_du_chapeau='15',
            couleur_du_chapeau='blanc',
            forme_du_chapeau='ovoide ',
            surface_du_chapeau='ecailleuse',
            type_de_marge='anodine',
            couleur_de_la_marge='neutre',
            dessous_du_chapeau='lamelles',
            couleur_au_dessous_du_chapeau='neutre',
            oxydation_du_chapeau='oxydation',
            couleur_de_l_oxydation_du_chapeau='bleu',
            mode_d_insertion_du_dessous_du_chapeau_avec_le_pied='libres',
            espace_entre_les_lamelles='serres',
            type_de_lamelles='normal',
            couleur_du_pied='neutre',
            pïed_creux_ou_plein='plein',
            forme_du_pied='pied long',
            surface_du_pied='rugeux',
            position_du_pied_par_rapport_au_chapeau='centrale',
            presence_d_un_anneau='oui',
            orientation_de_l_anneau='descendant',
            mobilite_de_l_anneau='non',
            couleur_de_l_anneau='neutre',
            poussee_en_touffe='non',
            couleur_de_la_base_du_pied='neutre',
            couleur_de_la_chair='neutre',
            oxydation_de_la_chair='oui',
            couleur_de_l_oxydation='bleu',
            fermete_de_la_chair='ferme',
            odeur='agreable',
            latex='oui',
            couleur_du_latex='neutre',
            mois_de_poussees_le_plus_tot='aout',
            mois_de_poussees_le_plus_tard='novembre',
            milieu='pres',
            pousse_sur_du_bois_ou_non='non',
            nom_vernaculaire='amanite test',
            comestibilite='toxique',
            commentaires='Ceci un commentaire test',
            synonymes='amanitas del testas',
            qq='qq test',
            image='testimage'
        )

        self.mock_brown_good = Mushroom.objects.create(
            id='3',
            espece='amanita testa 2',
            diametre_minimum_du_chapeau='10',
            diametre_maximum_du_chapeau='15',
            couleur_du_chapeau='brun',
            forme_du_chapeau='ovoide ',
            surface_du_chapeau='ecailleuse',
            type_de_marge='anodine',
            couleur_de_la_marge='neutre',
            dessous_du_chapeau='tubes',
            couleur_au_dessous_du_chapeau='neutre',
            oxydation_du_chapeau='oxydation',
            couleur_de_l_oxydation_du_chapeau='bleu',
            mode_d_insertion_du_dessous_du_chapeau_avec_le_pied='libres',
            espace_entre_les_lamelles='serres',
            type_de_lamelles='normal',
            couleur_du_pied='neutre',
            pïed_creux_ou_plein='plein',
            forme_du_pied='pied long',
            surface_du_pied='rugeux',
            position_du_pied_par_rapport_au_chapeau='centrale',
            presence_d_un_anneau='oui',
            orientation_de_l_anneau='descendant',
            mobilite_de_l_anneau='non',
            couleur_de_l_anneau='neutre',
            poussee_en_touffe='non',
            couleur_de_la_base_du_pied='neutre',
            couleur_de_la_chair='neutre',
            oxydation_de_la_chair='oui',
            couleur_de_l_oxydation='bleu',
            fermete_de_la_chair='ferme',
            odeur='agreable',
            latex='oui',
            couleur_du_latex='neutre',
            mois_de_poussees_le_plus_tot='aout',
            mois_de_poussees_le_plus_tard='novembre',
            milieu='pres',
            pousse_sur_du_bois_ou_non='non',
            nom_vernaculaire='amanite test',
            comestibilite='comestible',
            commentaires='Ceci un commentaire test',
            synonymes='amanitas del testas',
            qq='qq test',
            image='testimage'
        )

        self.list = [
            self.mock_mushroom,
            self.mock_white_toxic,
            self.mock_brown_good
        ]

    def test_get_all_mushrooms(self):

        service.get_all_mushrooms()
        self.assertEqual(self.mock_mushroom.espece, 'amanita testa')

    def test_set_mushroom_context(self):

        mushroom = self.mock_mushroom
        context = service.set_mushrooms_context(mushroom)
        for keys, vals in context.items():
            for key in keys:
                if key == "mushroom":
                    self.assertEqual(vals, self.mock_mushroom)

    def test_set_final_engine_context(self):

        mushroom = self.mock_mushroom
        context = service.set_final_engine_context(
            "rouge", "lamelles", "neutre", "oui", mushroom)
        key, value = 'color_top', 'rouge'
        self.assertTrue(key in context and value == context[key])
        key, value = 'form', 'lamelles'
        self.assertTrue(key in context and value == context[key])

    def test_get_mushroom(self):

        service.get_mushroom(1)
        self.assertEqual(self.mock_mushroom.espece, 'amanita testa')

    def test_search_results_with_name(self):

        service.search_results_with_name('amanita testa')
        self.assertEqual(self.mock_mushroom.espece, 'amanita testa')

    def test_sort_by_color_top_red(self):

        mushrooms = service.sort_by_color_top_red()
        self.assertEqual(mushrooms.count(), 1)

    def test_sort_by_color_top_white(self):

        mushrooms = service.sort_by_color_top_white()
        self.assertEqual(mushrooms.count(), 1)

    def test_sort_by_color_top_yellow(self):

        mushrooms = service.sort_by_color_top_yellow()
        self.assertEqual(mushrooms.count(), 0)

    def test_sort_by_color_top_brown(self):

        mushrooms = service.sort_by_color_top_brown()
        self.assertEqual(mushrooms.count(), 1)

    def test_sort_by_color_top_other(self):

        mushrooms = service.sort_by_color_top_other()
        self.assertEqual(mushrooms.count(), 0)

    def test_sort_by_lamelles(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_lamelles(list_id)
        self.assertEqual(mushrooms.count(), 2
                         )

    def test_sort_by_tubes(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_tubes(list_id)
        self.assertEqual(mushrooms.count(), 1
                         )

    def test_sort_by_plis(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_plis(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_aiguillons(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_aiguillons(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_no_lamelles_and_tubes(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_no_lamelles_and_tubes(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_color_under_white(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_color_under_white(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_color_under_brown(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_color_under_brown(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_color_under_yellow(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_color_under_yellow(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_color_under_red(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_color_under_red(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_color_under_other(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_color_under_other(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_sort_by_ring(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_ring(list_id)
        self.assertEqual(mushrooms.count(), 3
                         )

    def test_sort_by_not_ring(self):

        list_id = []
        for element in self.list:
            list_id.append(element.id)

        mushrooms = service.sort_by_not_ring(list_id)
        self.assertEqual(mushrooms.count(), 0
                         )

    def test_manage_add_favorite(self):

        # 1) ADD THE FAVORITE and check that user ID exist
        service.add_or_remove_favorite(
            self.mock_mushroom, self.mock_user)
        for value in self.mock_mushroom.favorites.values():
            self.assertEqual(value["id"], self.mock_user.id)

        # 2) ADD THE FAVORITE and check that there is no more user ID
        service.add_or_remove_favorite(
            self.mock_mushroom, self.mock_user)
        for value in self.mock_mushroom.favorites.values():
            self.assertEqual(value["id"], None)

    def test_setup_favorites_list_context(self):
        """Test that the context of the method is correctly set"""

        favorites = [self.mock_mushroom, self.mock_white_toxic]
        context = service.setup_favorites_list_context(
            favorites)
        for keys, vals in context.items():
            for key in keys:
                if key == "favorites":
                    self.assertEqual(vals, favorites)

    def test_sort_out_user_favorite_mushrooms(self):
        """
        Test that the method will return correctly that the 1st product mock
        is in user mock favorites from a list with the two product mocks
        """

        self.mock_mushroom.favorites.add("1")
        mushrooms = [self.mock_mushroom, self.mock_white_toxic]
        service.sort_out_user_favorite_mushrooms(
            mushrooms, self.mock_user)
        self.assertEqual(self.mock_mushroom.is_fav, True)
        self.assertEqual(self.mock_white_toxic.is_fav, False)

    def test_sort_out_if_mushroom_is_favorite_is_true(self):
        """
        Test that the method will return correctly that a product mock
        is in user mock favorites
        """

        self.mock_mushroom.favorites.add("1")
        service.sort_out_if_mushroom_is_favorite(
            self.mock_mushroom, self.mock_user)
        self.assertEqual(self.mock_mushroom.is_fav, True)

    def test_sort_out_if_mushroom_is_favorite_is_false(self):
        """
        Test that the method will return correctly that a product mock
        is in user mock favorites
        """

        service.sort_out_if_mushroom_is_favorite(
            self.mock_mushroom, self.mock_user)
        self.assertEqual(self.mock_mushroom.is_fav, False)
