from django.db import models

# Create your models here.
class Auto(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)