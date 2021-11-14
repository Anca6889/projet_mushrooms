from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from interface.models import Mushroom
from progress.bar import FillingSquaresBar
import requests
import json


class Command(BaseCommand):

    def launch_process(self):
        """Launch the all process"""

        print("regen database process launched...")
        self.clear_db()

    def clear_db(self):
        """Delete all datas in DB"""

        print("dropping actual database...")
        mushroom_obj = Mushroom.objects.all()
        mushroom_obj.delete()
        print("database cleared !")
        self.load_data()

    def load_data(self):
        """Load the data in DB from json file"""
        with open('public_ressources/base-de-donnees-champignons.json') as data:
            data_dict = json.load(data)
            self.insert_mushrooms_in_db(data_dict)

    def insert_mushrooms_in_db(self, data_dict):

        with FillingSquaresBar(
            "Poping database...",
                max=len(data_dict), suffix="%(percent)d%%") as bar:

            for mushroom in data_dict:

                try:
                    espece = mushroom['Espece']
                    diametre_minimum_du_chapeau = mushroom['Diametre minimum du chapeau']
                    diametre_maximum_du_chapeau = mushroom['Diametre maximum du chapeau']
                    couleur_du_chapeau = mushroom['Couleur du chapeau']
                    forme_du_chapeau = mushroom['Forme du chapeau']
                    surface_du_chapeau = mushroom['Surface du chapeau']
                    type_de_marge = mushroom['Type de marge']
                    couleur_de_la_marge = mushroom['Couleur de la marge']
                    dessous_du_chapeau = mushroom['Dessous du chapeau']
                    couleur_au_dessous_du_chapeau = mushroom['Couleur au dessous du chapeau']
                    oxydation_du_chapeau = mushroom['Oxydation du chapeau']
                    couleur_de_l_oxydation_du_chapeau = mushroom['Couleur de l oxydation du chapeau']
                    mode_d_insertion_du_dessous_du_chapeau_avec_le_pied = mushroom[
                        'Mode d insertion du dessous du chapeau avec le pied']
                    espace_entre_les_lamelles = mushroom['Espace entre les lamelles']
                    type_de_lamelles = mushroom['Type de lamelles']
                    couleur_du_pied = mushroom['Couleur du pied']
                    pïed_creux_ou_plein = mushroom['Forme du pied']
                    forme_du_pied = mushroom['Longueur du pied']
                    surface_du_pied = mushroom['Surface su pied']
                    position_du_pied_par_rapport_au_chapeau = mushroom[
                        'Position du pied par rapport au chapeau']
                    presence_d_un_anneau = mushroom['Presence d un anneau']
                    orientation_de_l_anneau = mushroom['Orientation de l anneau']
                    mobilite_de_l_anneau = mushroom['Mobilite de l anneau']
                    couleur_de_l_anneau = mushroom['Couleur de l anneau']
                    poussee_en_touffe = mushroom['Poussee en touffe']
                    couleur_de_la_base_du_pied = mushroom['Couleur de la base du pied']
                    couleur_de_la_chair = mushroom['Couleur de la chair']
                    oxydation_de_la_chair = mushroom['Oxydation de la chair']
                    couleur_de_l_oxydation = mushroom['Couleur de l oxydation']
                    fermete_de_la_chair = mushroom['Fermete de la chair']
                    odeur = mushroom['Odeur']
                    latex = mushroom['Latex']
                    couleur_du_latex = mushroom['Couleur du latex']
                    mois_de_poussees_le_plus_tot = mushroom['Mois de poussees le plus tot']
                    mois_de_poussees_le_plus_tard = mushroom['Mois de poussees le plus tard']
                    milieu = mushroom['Milieu']
                    pousse_sur_du_bois_ou_non = mushroom['Pousse sur du bois ou non']
                    nom_vernaculaire = mushroom['Nom vernaculaire']
                    comestibilite = mushroom['Comestibilite']
                    commentaires = mushroom['Commentaires']
                    synonymes = mushroom['Synonymes']
                    qq = mushroom['FIELD43']

                    try:

                        Mushroom.objects.get_or_create(
                            espece=espece,
                            diametre_minimum_du_chapeau=diametre_minimum_du_chapeau,
                            diametre_maximum_du_chapeau=diametre_maximum_du_chapeau,
                            couleur_du_chapeau=couleur_du_chapeau,
                            forme_du_chapeau=forme_du_chapeau,
                            surface_du_chapeau=surface_du_chapeau,
                            type_de_marge=type_de_marge,
                            couleur_de_la_marge=couleur_de_la_marge,
                            dessous_du_chapeau=dessous_du_chapeau,
                            couleur_au_dessous_du_chapeau=couleur_au_dessous_du_chapeau,
                            oxydation_du_chapeau=oxydation_du_chapeau,
                            couleur_de_l_oxydation_du_chapeau=couleur_de_l_oxydation_du_chapeau,
                            mode_d_insertion_du_dessous_du_chapeau_avec_le_pied=mode_d_insertion_du_dessous_du_chapeau_avec_le_pied,
                            espace_entre_les_lamelles=espace_entre_les_lamelles,
                            type_de_lamelles=type_de_lamelles,
                            couleur_du_pied=couleur_du_pied,
                            pïed_creux_ou_plein=pïed_creux_ou_plein,
                            forme_du_pied=forme_du_pied,
                            surface_du_pied=surface_du_pied,
                            position_du_pied_par_rapport_au_chapeau=position_du_pied_par_rapport_au_chapeau,
                            presence_d_un_anneau=presence_d_un_anneau,
                            orientation_de_l_anneau=orientation_de_l_anneau,
                            mobilite_de_l_anneau=mobilite_de_l_anneau,
                            couleur_de_l_anneau=couleur_de_l_anneau,
                            poussee_en_touffe=poussee_en_touffe,
                            couleur_de_la_base_du_pied=couleur_de_la_base_du_pied,
                            couleur_de_la_chair=couleur_de_la_chair,
                            oxydation_de_la_chair=oxydation_de_la_chair,
                            couleur_de_l_oxydation=couleur_de_l_oxydation,
                            fermete_de_la_chair=fermete_de_la_chair,
                            odeur=odeur,
                            latex=latex,
                            couleur_du_latex=couleur_du_latex,
                            mois_de_poussees_le_plus_tot=mois_de_poussees_le_plus_tot,
                            mois_de_poussees_le_plus_tard=mois_de_poussees_le_plus_tard,
                            milieu=milieu,
                            pousse_sur_du_bois_ou_non=pousse_sur_du_bois_ou_non,
                            nom_vernaculaire=nom_vernaculaire,
                            comestibilite=comestibilite,
                            commentaires=commentaires,
                            synonymes=synonymes,
                            qq=qq
                        )[0]

                    except KeyError:
                        pass

                    except DataError:
                        pass

                    except IntegrityError:
                        pass

                    bar.next()

                except KeyError:
                    pass
        bar.finish()

    def handle(self, *args, **options):
        """Alow to use the Django command 'manage.py database'"""

        self.launch_process()
