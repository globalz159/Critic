from django.db import models

from core.models import Usuario

class Like(models.Model):
    LIKE_CHOICES = (
        (1, 'Like'),
        (2, 'Deslike')
    )
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="user_id")
    like = models.IntegerField("Like", choices=LIKE_CHOICES)


class Comentario(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario_pai = models.ForeignKey("Comentario", on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(Like, symmetrical=False)
    texto = models.TextField("Comentario")
