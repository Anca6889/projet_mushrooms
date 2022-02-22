"""This module will use selenium for testing with Google Chrome Navigator"""
from projectmushrooms.settings import BASE_DIR
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from interface.models import Mushroom


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')


class BrowserTests(StaticLiveServerTestCase):
    """This class will test a product research and click on legals link"""

    def setUp(self):
        """setup the webdriver with Google Chrome driver"""

        self.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,
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

    def test_search_product(self):
        """This method will do all the actions, check comments below"""

        # go to main page
        self.driver.get(self.live_server_url)

        # find search bar and send value nutella, find search button and click
        search = self.driver.find_element_by_name("search")
        top_search_button = self.driver.find_element_by_id("top-search-button")
        search.send_keys("amanita testa")
        top_search_button.click()
        mushroom_details = self.driver.find_element_by_name("details")
        mushroom_details.click()

