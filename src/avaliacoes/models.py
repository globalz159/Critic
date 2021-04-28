from django.db import models

from core.models import Usuario

class Avaliacao(models.Model):
    VALOR_CHOICES = (
        (1, 'Péssimo'),
        (2, 'Ruim'),
        (3, 'Normal'),
        (4, 'Legal'),
        (5, 'Muito bom')
    )

    valor = models.IntegerField("Avaliação", choices=VALOR_CHOICES)
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="user_id")
    msg = models.TextField("Mensagem")

