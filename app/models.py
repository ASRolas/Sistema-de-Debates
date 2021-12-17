from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=150)
    senha = models.CharField(max_length=100)

class Postagem(models.Model):
    titulo = models.CharField(max_length=150)
    data = models.CharField(max_length=100)
    postagem = models.CharField(max_length=100)
    postador = models.CharField(max_length=100)
