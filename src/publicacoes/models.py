from django.db import models

from core.models import Usuario


class Publicacao(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="user_id")
    
    # Comentarios = Publicacao.objects.first().comentario_set.all()

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"


class LikePub(models.Model):
    LIKE_CHOICES = (
        (1, 'Like'),
        (2, 'Deslike')
    )
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id")
    like = models.IntegerField("Like", choices=LIKE_CHOICES)
