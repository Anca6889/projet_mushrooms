"""This module will test the views"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from interface.models import Mushroom


class Viewstests(TestCase):
    """
    This class test all the views
    As most of the methods of the views are contained in interface/service.py,
    The only thing we still have to test is that the views return the correct
    templates. It'neccesary to mock a user, a product and catch all the urls.
    Each method name describe exactly which view is tested.
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

        self.client = Client()
        self.main = reverse("index")
        self.info = reverse("info")
        self.atoz = reverse("atoz")
        self.search_list = reverse("search_list")+"?search=testname"
        self.mushroom_details = reverse("mushroom", args=[1])
        self.sort_by_edible_very_good = reverse("sort_by_edible_very_good")
        self.sort_by_edible_good = reverse("sort_by_edible_good")
        self.sort_by_edible_bad_good = reverse("sort_by_edible_bad_good")
        self.sort_by_edible_bad = reverse("sort_by_edible_bad")
        self.sort_by_edible_toxic = reverse("sort_by_edible_toxic")
        self.sort_by_edible_deadly = reverse("sort_by_edible_deadly")
        self.engine2 = reverse("engine2", args=['neutre'])
        self.engine3 = reverse("engine3", args=['neutre', 'lamelles'])
        self.engine4 = reverse("engine4", args=['neutre', 'lamelles', 'neutre'])
        self.engine_results = reverse("engine_results", args=[
                                      'neutre', 'lamelles', 'neutre', 'oui'])

    def test_main_view(self):
        response = self.client.get(self.main)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_info(self):
        response = self.client.get(self.info)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info.html")

    def test_atoz(self):
        response = self.client.get(self.atoz)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "atoz.html")

    def test_search_list(self):
        response = self.client.get(self.search_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search_list.html")

    def test_mushroom_details(self):
        response = self.client.get(self.mushroom_details)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mushroom_details.html")

    def test_sort_by_edible_very_good(self):
        response = self.client.get(self.sort_by_edible_very_good)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_very_good.html")

    def test_sort_by_edible_good(self):
        response = self.client.get(self.sort_by_edible_good)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_good.html")

    def test_sort_by_edible_bad_good(self):
        response = self.client.get(self.sort_by_edible_bad_good)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_bad_good.html")

    def test_sort_by_edible_bad(self):
        response = self.client.get(self.sort_by_edible_bad)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_bad.html")

    def test_sort_by_edible_toxic(self):
        response = self.client.get(self.sort_by_edible_toxic)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_toxic.html")

    def test_sort_by_edible_deadly(self):
        response = self.client.get(self.sort_by_edible_deadly)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sort_by_edible_deadly.html")

    def test_engine2(self):
        response = self.client.get(self.engine2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "engine2.html")

    def test_engine3(self):
        response = self.client.get(self.engine3)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "engine3.html")

    def test_engine4(self):
        response = self.client.get(self.engine4)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "engine4.html")

    def test_engine_results(self):
        response = self.client.get(self.engine_results)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "engine_results.html")
