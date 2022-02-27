App in French.
____
# FUNGI FINDER, Identifier facilement des champignons que vous trouvez lors de vos randonnées (French)

FUNGI FINDER est une application web qui permet d'identifier et de trier des champignons selon des critères de commestibilités. Grâce a un moteur d'identification à 4 clics, identifiez très facilement vos champignons.
 
Ce projet est en Français et fonctionne avec l'API de Wikipédia et les données mise à disposition par Mr. Mathieu Andro que je remercie. Ces données sont disponible à cette adresse => https://www.data.gouv.fr/fr/datasets/donnees-du-site-identifier-les-champignons-com/
____


## Lien de l'application déployée sur HEROKU ;-) 

https://fungifinder.herokuapp.com/

____
## Utiliser l'app sur votre machine local:

- Assurez vous d'avoir python 3 et pip installé sur votre machine
- Vous devez disposer d'une base de donnée POSTGRE SQL
- Clonez ce dépôt sur votre Machine locale
- Installez et initialisez pipenv
- Configurer votre base de données dans P8_pur_beurre\settings.py => DATABASE
- Definissez une SECRET_KEY dans vos variables d'environements
- Lancer le shell de pipenv
- Effectuer les migrations
- Lancer le téléchargement et peuplement de la base de données
- Lancer le serveur local

____
## Commands :

Installer pipenv:  
``` py -m pip install pipenv ```  

Installer toutes les dépendances du projet:  
``` py -m pipenv install ```  

Lancer le shell pipenv:  
``` py -m pipenv shell ```  

Configurer les migrations:  
``` py manage.py makemigrations ```  

Executer les migrations:  
``` py manage.py migrate ```  

Appel à l'API et peupler la BDD:  
``` py manage.py pop_db ```  
``` py manage.py get_picts.py ```  
``` py manage.py get_aditional_picts.py ```  

Lancer le serveur local:  
``` py manage.py runserver ```  

Lancer les tests (si nécessaire):  
``` py manage.py test ```  

Lancer les tests avec coverage:  
``` coverage run --source='.' manage.py test -v2 ```

Rapport coverage:  
``` coverage report ```
___
## Paquets utilisés :

[packages]  
django = "*"  
psycopg2 = "*"  
requests = "*"  
progress = "*"  
wikipedia = "*"  
django-crispy-forms = "*"  
coverage = "*"  
flake8 = "*"  
django-heroku = "*"  
gunicorn = "*"  
sentry-sdk = "*"  
whitenoise = "*"  
selenium = "*"  

[requires]  
python_version = "3.9"  




