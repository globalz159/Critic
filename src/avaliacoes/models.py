from django.db import models

from core.models import Usuario
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

    data_criacao = models.DateField(auto_now=True, blank=True), 
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", blank=True)
    valor = models.IntegerField("Avaliação", choices=VALOR_CHOICES)
    avaliacao = models.CharField("Comentário", max_length=200, null=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        abstract = True

class AvaliacaoFilme(Avaliacao):
    item = models.ForeignKey(Filme, on_delete=models.CASCADE, blank=True)

    def curtir(self, user_id):
        like = LikeAvaliacaoFilme(user_id=user_id, avaliacao=self)
        like.save()

class AvaliacaoLivro(Avaliacao):
    item = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=True)
    
    def curtir(self, user_id):
        like = LikeAvaliacaoLivro(user_id=user_id, avaliacao=self)
        like.save()

class AvaliacaoSerie(Avaliacao):
    item = models.ForeignKey(Serie, on_delete=models.CASCADE, blank=True)

    def curtir(self, user_id):
        like = LikeAvaliacaoSerie(user_id=user_id, avaliacao=self)
        like.save()

class LikeAv(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", blank=True)
    class Meta:
        abstract = True
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

class LikeAvaliacaoFilme(LikeAv):
    avaliacao = models.ForeignKey(AvaliacaoFilme, on_delete=models.CASCADE)

class LikeAvaliacaoLivro(LikeAv):
    avaliacao = models.ForeignKey(AvaliacaoLivro, on_delete=models.CASCADE)

class LikeAvaliacaoSerie(LikeAv):
    avaliacao = models.ForeignKey(AvaliacaoSerie, on_delete=models.CASCADE)