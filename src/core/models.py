from django.db import models

class Usuario(models.Model):
    nome = models.CharField("Nome", max_length=255)
    sobrenome = models.CharField("Sobrenome", max_length=255)
    estado = models.CharField("Estado", max_length=100)
    cidade = models.CharField("Cidade", max_length=100)
    username = models.CharField("Nome de Usuário", max_length=30)
    email = models.EmailField("Email", max_length=255)
    senha = models.CharField("Senha", max_length=100)



