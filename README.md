# akhikachmoney_conteneur
$ docker-compose build
$ docker-compose run --rm connexion django-admin startproject connexion .
$ docker-compose run --rm connexion python3 manage.py startapp utilisateurs .
$ docker-compose run --rm connexion python3 manage.py migrate
$ docker-compose run --rm connexion python3 manage.py createsuperuser
$ docker-compose up
$ docker-compose run --rm connexion python3 manage.py makemigrations
