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
    comentario_pai = models.ForeignKey('ComentarioFilme', on_delete=models.CASCADE, null=True)
    
    def curtir(self, user_id):
        like = LikeComentarioFilme(user_id=user_id, comentario=self)
        like.save()

    def descurtir(self, user_id):
        like = LikeComentarioFilme.objects.get(user_id=user_id)
        like.delete()

class ComentarioLivro(Comentario):
    avaliacao = models.ForeignKey(AvaliacaoLivro, on_delete=models.CASCADE, verbose_name="avaliacao")
    comentario_pai = models.ForeignKey('ComentarioLivro', on_delete=models.CASCADE, null=True)

    def curtir(self, user_id):
        like = LikeComentarioLivro(user_id=user_id, comentario=self)
        like.save()

    def descurtir(self, user_id):
        like = LikeComentarioLivro.objects.get(user_id=user_id)
        like.delete()

class ComentarioSerie(Comentario):
    avaliacao = models.ForeignKey(AvaliacaoSerie, on_delete=models.CASCADE, verbose_name="avaliacao")
    comentario_pai = models.ForeignKey('ComentarioSerie', on_delete=models.CASCADE, null=True)

    def curtir(self, user_id):
        like = LikeComentarioSerie(user_id=user_id, comentario=self)
        like.save()

    def descurtir(self, user_id):
        like = LikeComentarioSerie.objects.get(user_id=user_id)
        like.delete()

class LikeComentario(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id")

    class Meta:
        abstract = True

class LikeComentarioFilme(LikeComentario):
    comentario = models.ForeignKey(ComentarioFilme, on_delete=models.CASCADE)

class LikeComentarioLivro(LikeComentario):
    comentario = models.ForeignKey(ComentarioLivro, on_delete=models.CASCADE)

class LikeComentarioSerie(LikeComentario):
    comentario = models.ForeignKey(ComentarioSerie, on_delete=models.CASCADE)
