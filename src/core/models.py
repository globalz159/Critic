from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # PK = username
    # os campos: username, password, email, first_name, last_name vem de AbstractUser
    
    estado = models.CharField("Estado", max_length=100)
    cidade = models.CharField("Cidade", max_length=100)
    data_nascimento = models.DateField("Data de Nascimento", null=True)



