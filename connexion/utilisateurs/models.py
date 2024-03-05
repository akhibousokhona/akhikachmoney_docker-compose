from django.db import models
import time
from datetime import date
from django.contrib.auth.models import AbstractUser
 
# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_exp = models.CharField(max_length=255)
    prenom_exp = models.CharField(max_length=255)
    phone_exp = models.CharField(max_length=255)
    nom_benef = models.CharField(max_length=255)
    prenom_benef = models.CharField(max_length=255)
    phone_benef = models.CharField(max_length=255)
    date_transaction = models.DateField()
    commission =  models.IntegerField()
    montant =  models.IntegerField()
    total =  models.IntegerField()
    code =  models.IntegerField()
    status = models.CharField(max_length=255)
    type_piece = models.CharField(max_length=255)
    numero_piece = models.CharField(max_length=255)
##