# Generated by Django 3.2.7 on 2021-09-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mushroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espece', models.CharField(max_length=200)),
                ('diametre_minimum_du_chapeau', models.CharField(max_length=4)),
                ('diametre_maximum_du_chapeau', models.CharField(max_length=4)),
                ('couleur_du_chapeau', models.CharField(max_length=200)),
                ('forme_du_chapeau', models.CharField(max_length=1000)),
                ('surface_du_chapeau', models.CharField(max_length=1000)),
                ('type_de_marge', models.CharField(max_length=1000)),
                ('couleur_de_la_marge', models.CharField(max_length=200)),
                ('dessous_du_chapeau', models.CharField(max_length=200)),
                ('couleur_au_dessous_du_chapeau', models.CharField(max_length=200)),
                ('oxydation_du_chapeau', models.CharField(max_length=200)),
                ('couleur_de_l_oxydation_du_chapeau', models.CharField(max_length=200)),
                ('mode_d_insertion_du_dessous_du_chapeau_avec_le_pied', models.CharField(max_length=200)),
                ('espace_entre_les_lamelles', models.CharField(max_length=200)),
                ('type_de_lamelles', models.CharField(max_length=200)),
                ('couleur_du_pied', models.CharField(max_length=200)),
                ('pïed_creux_ou_plein', models.CharField(max_length=200)),
                ('forme_du_pied', models.CharField(max_length=200)),
                ('surface_du_pied', models.CharField(max_length=200)),
                ('position_du_pied_par_rapport_au_chapeau', models.CharField(max_length=200)),
                ('presence_d_un_anneau', models.CharField(max_length=200)),
                ('orientation_de_l_anneau', models.CharField(max_length=200)),
                ('mobilite_de_l_anneau', models.CharField(max_length=200)),
                ('couleur_de_l_anneau', models.CharField(max_length=200)),
                ('poussee_en_touffe', models.CharField(max_length=200)),
                ('couleur_de_la_base_du_pied', models.CharField(max_length=200)),
                ('couleur_de_la_chair', models.CharField(max_length=200)),
                ('oxydation_de_la_chair', models.CharField(max_length=200)),
                ('couleur_de_l_oxydation', models.CharField(max_length=200)),
                ('fermete_de_la_chair', models.CharField(max_length=200)),
                ('odeur', models.CharField(max_length=200)),
                ('latex', models.CharField(max_length=200)),
                ('couleur_du_latex', models.CharField(max_length=200)),
                ('mois_de_poussees_le_plus_tot', models.CharField(max_length=200)),
                ('mois_de_poussees_le_plus_tard', models.CharField(max_length=200)),
                ('milieu', models.CharField(max_length=200)),
                ('pousse_sur_du_bois_ou_non', models.CharField(max_length=200)),
                ('nom_vernaculaire', models.CharField(max_length=1000)),
                ('comestibilite', models.CharField(max_length=200)),
                ('commentaires', models.CharField(max_length=4000)),
                ('synonymes', models.CharField(max_length=2000)),
                ('qq', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=2000, null=True)),
            ],
        ),
    ]
