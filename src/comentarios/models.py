from django.db import models
from avaliacoes.models import *

from core.models import Usuario
from avaliacoes.models import *

class Comentario(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField("Comentario", max_length="1024")

    class Meta:
        abstract = True
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    
    def __str__(self):
        return f"{self.avaliacao.id}: {self.texto}"


class ComentarioFilme(Comentario):
    avaliacao = models.ForeignKey(AvaliacaoFilme, on_delete=models.CASCADE, verbose_name="avaliacao")

class ComentarioLivro(Comentario):
    avaliacao = models.ForeignKey(AvaliacaoLivro, on_delete=models.CASCADE, verbose_name="avaliacao")

class ComentarioSerie(Comentario):
    avaliacao = models.ForeignKey(AvaliacaoSerie, on_delete=models.CASCADE, verbose_name="avaliacao")
    


class LikeComentario(models.Model):
    LIKE_CHOICES = (
        (1, 'Like'),
        (2, 'Deslike')
    )
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id")
    like = models.IntegerField("Like", choices=LIKE_CHOICES)

    class Meta:
        abstract = True

class LikeComentarioFilme(LikeComentario):
    comentario = models.ForeignKey(ComentarioFilme, on_delete=models.CASCADE)

class LikeComentarioLivro(LikeComentario):
    comentario = models.ForeignKey(ComentarioLivro, on_delete=models.CASCADE)

class LikeComentarioSerie(LikeComentario):
    comentario = models.ForeignKey(ComentarioSerie, on_delete=models.CASCADE)
