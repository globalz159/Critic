from django.db import models

class Usuarios(models.Model):
    nome = models.CharField("Nome", max_length=255)
    sobrenome = models.CharField("Nome", max_length=255)

