####################### lancement du projet dans docker-compose ########################
$ sudo docker-compose build
$ sudo docker-compose up
################################## pour la creation d'un projet #############
$ docker-compose run --rm connexion django-admin startproject connexion .
################################## pour la creation d'une application #############
$ docker-compose run --rm connexion python3 manage.py startapp utilisateurs .
################################## pour la creation d'une application #############
################################## mise à jour de bd#############
$ docker-compose run --rm connexion python3 manage.py migrate
$ docker-compose run --rm connexion python3 manage.py makemigrations
################################## creer un super utilisateur #############
$ docker-compose run --rm connexion python3 manage.py createsuperuser

