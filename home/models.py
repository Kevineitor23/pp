from django.db import models

class contacto(models.Model):
    name = models.CharField(max_length=100)
    numero = models.IntegerField()