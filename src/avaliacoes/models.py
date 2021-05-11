from django.db import models

from core.models import Usuario
from comentarios.models import Comentario
from itens.models import Filme, Livro, Serie


class Avaliacao(models.Model):
    VALOR_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    valor = models.IntegerField("Avaliação", choices=VALOR_CHOICES)
    
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="user_id")
    
    class Meta:
        abstract = True

class AvaliacaoFilme(Avaliacao):
    item = models.ForeignKey(Filme, on_delete=models.CASCADE)

class AvaliacaoLivro(Avaliacao):
    item = models.ForeignKey(Livro, on_delete=models.CASCADE)

class AvaliacaoSerie(Avaliacao):
    item = models.ForeignKey(Serie, on_delete=models.CASCADE)