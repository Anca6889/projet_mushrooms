"""This module will test the views"""

from django.test import TestCase
from interface.models import Mushroom


class Modelstests(TestCase):
    """
    This class will mock a fake mushroom and will tests if
    all the atributes from the fake database are matching.
    """

    def setUp(self):
        """Setup the mock"""

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

    def test_id(self):
        result = self.mock_mushroom.id
        self.assertEqual(result, 1)

    def test_espece(self):
        result = self.mock_mushroom.espece
        self.assertEqual(result, 'amanita testa')

    def test_diametre_minimum_du_chapeau(self):
        result = self.mock_mushroom.diametre_minimum_du_chapeau
        self.assertEqual(result, '10')

    def test_diametre_maximum_du_chapeau(self):
        result = self.mock_mushroom.diametre_maximum_du_chapeau
        self.assertEqual(result, '15')

    def test_couleur_du_chapeau(self):
        result = self.mock_mushroom.couleur_du_chapeau
        self.assertEqual(result, 'rouge')

    def test_forme_du_chapeau(self):
        result = self.mock_mushroom.forme_du_chapeau
        self.assertEqual(result, 'ovoide ')

    def test_surface_du_chapeau(self):
        result = self.mock_mushroom.surface_du_chapeau
        self.assertEqual(result, 'ecailleuse')

    def test_type_de_marge(self):
        result = self.mock_mushroom.type_de_marge
        self.assertEqual(result, 'anodine')

    def test_couleur_de_la_marge(self):
        result = self.mock_mushroom.couleur_de_la_marge
        self.assertEqual(result, 'neutre')

    def test_dessous_du_chapeau(self):
        result = self.mock_mushroom.dessous_du_chapeau
        self.assertEqual(result, 'lamelles')

    def test_couleur_au_dessous_du_chapeau(self):
        result = self.mock_mushroom.couleur_au_dessous_du_chapeau
        self.assertEqual(result, 'neutre')

    def test_oxydation_du_chapeau(self):
        result = self.mock_mushroom.oxydation_du_chapeau
        self.assertEqual(result, 'oxydation')

    def test_couleur_de_l_oxydation_du_chapeau(self):
        result = self.mock_mushroom.couleur_de_l_oxydation_du_chapeau
        self.assertEqual(result, 'bleu')

    def test_mode_d_insertion_du_dessous_du_chapeau_avec_le_pied(self):
        result = self.mock_mushroom.mode_d_insertion_du_dessous_du_chapeau_avec_le_pied
        self.assertEqual(result, 'libres')

    def test_espace_entre_les_lamelles(self):
        result = self.mock_mushroom.espace_entre_les_lamelles
        self.assertEqual(result, 'serres')

    def test_type_de_lamelles(self):
        result = self.mock_mushroom.type_de_lamelles
        self.assertEqual(result, 'normal')

    def test_couleur_du_pied(self):
        result = self.mock_mushroom.couleur_du_pied
        self.assertEqual(result, 'neutre')

    def test_pïed_creux_ou_plein(self):
        result = self.mock_mushroom.pïed_creux_ou_plein
        self.assertEqual(result, 'plein')

    def test_forme_du_pied(self):
        result = self.mock_mushroom.forme_du_pied
        self.assertEqual(result, 'pied long')

    def test_surface_du_pied(self):
        result = self.mock_mushroom.surface_du_pied
        self.assertEqual(result, 'rugeux')

    def test_position_du_pied_par_rapport_au_chapeau(self):
        result = self.mock_mushroom.position_du_pied_par_rapport_au_chapeau
        self.assertEqual(result, 'centrale')

    def test_presence_d_un_anneau(self):
        result = self.mock_mushroom.presence_d_un_anneau
        self.assertEqual(result, 'oui')

    def test_orientation_de_l_anneau(self):
        result = self.mock_mushroom.orientation_de_l_anneau
        self.assertEqual(result, 'descendant')

    def test_mobilite_de_l_anneau(self):
        result = self.mock_mushroom.mobilite_de_l_anneau
        self.assertEqual(result, 'non')

    def test_couleur_de_l_anneau(self):
        result = self.mock_mushroom.couleur_de_l_anneau
        self.assertEqual(result, 'neutre')

    def test_poussee_en_touffe(self):
        result = self.mock_mushroom.poussee_en_touffe
        self.assertEqual(result, 'non')

    def test_couleur_de_la_base_du_pied(self):
        result = self.mock_mushroom.couleur_de_la_base_du_pied
        self.assertEqual(result, 'neutre')

    def test_couleur_de_la_chair(self):
        result = self.mock_mushroom.couleur_de_la_chair
        self.assertEqual(result, 'neutre')

    def test_oxydation_de_la_chair(self):
        result = self.mock_mushroom.oxydation_de_la_chair
        self.assertEqual(result, 'oui')

    def test_couleur_de_l_oxydation(self):
        result = self.mock_mushroom.couleur_de_l_oxydation
        self.assertEqual(result, 'bleu')

    def test_fermete_de_la_chair(self):
        result = self.mock_mushroom.fermete_de_la_chair
        self.assertEqual(result, 'ferme')

    def test_odeur(self):
        result = self.mock_mushroom.odeur
        self.assertEqual(result, 'agreable')

    def test_latex(self):
        result = self.mock_mushroom.latex
        self.assertEqual(result, 'oui')

    def test_couleur_du_latex(self):
        result = self.mock_mushroom.couleur_du_latex
        self.assertEqual(result, 'neutre')

    def test_mois_de_poussees_le_plus_tot(self):
        result = self.mock_mushroom.mois_de_poussees_le_plus_tot
        self.assertEqual(result, 'aout')

    def test_mois_de_poussees_le_plus_tard(self):
        result = self.mock_mushroom.mois_de_poussees_le_plus_tard
        self.assertEqual(result, 'novembre')

    def test_milieu(self):
        result = self.mock_mushroom.milieu
        self.assertEqual(result, 'pres')

    def test_pousse_sur_du_bois_ou_non(self):
        result = self.mock_mushroom.pousse_sur_du_bois_ou_non
        self.assertEqual(result, 'non')

    def test_nom_vernaculaire(self):
        result = self.mock_mushroom.nom_vernaculaire
        self.assertEqual(result, 'amanite test')

    def test_comestibilite(self):
        result = self.mock_mushroom.comestibilite
        self.assertEqual(result, 'toxique')

    def test_commentaires(self):
        result = self.mock_mushroom.commentaires
        self.assertEqual(result, 'Ceci un commentaire test')

    def test_synonymes(self):
        result = self.mock_mushroom.synonymes
        self.assertEqual(result, 'amanitas del testas')

    def test_qq(self):
        result = self.mock_mushroom.qq
        self.assertEqual(result, 'qq test')

    def test_image(self):
        result = self.mock_mushroom.image
        self.assertEqual(result, 'testimage')

    def test___str__(self):
        result = self.mock_mushroom.__str__()
        self.assertEqual(result, 'amanita testa')
