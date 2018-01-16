from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Usuari(models.Model):
    nombre = models.CharField(max_length = 40)
    correos = models.CharField(primary_key=True,max_length = 40)
    contrasena = models.CharField(max_length = 20)

#class Meta():
#        db_table = 'auth_user'
