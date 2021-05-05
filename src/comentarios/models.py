from django.db import models

from core.models import Usuario
from publicacoes.models import Publicacao

class Comentario(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE, default=False)
    comentario_pai = models.ForeignKey("Comentario", on_delete=models.CASCADE, null=True, blank=True)
    texto = models.TextField("Comentario", max_length="500")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    
    def __str__(self):
        return f"{self.publicacao.id}: {self.texto}"


class Like(models.Model):
    LIKE_CHOICES = (
        (1, 'Like'),
        (2, 'Deslike')
    )
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="user_id")
    like = models.IntegerField("Like", choices=LIKE_CHOICES)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, default=False)
