from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    imagen = models.ImageField(upload_to="portadas",null = False, blank = True)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=1000)


