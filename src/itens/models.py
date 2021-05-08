from datetime import datetime
from avaliacoes.models import Avaliacao

from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify
from stdimage.models import StdImageField

class Itens(models.Model):
    data_criacao = models.DateField("Data de Criação", auto_now_add=True, null=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)
    ativo = models.BooleanField("Ativo", default=True)
    titulo = models.CharField("Título", max_length=100)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.DateField("Ano de lançamento")
    slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)
    imagem = StdImageField("Imagem de capa", null=True, upload_to='itens', variations={'thumb': (124, 124)})

    avaliacoes = models.ManyToManyField(Avaliacao)
    ativo = models.BooleanField("Ativo", default=False)

    class Meta:
        abstract = True

class Livro(Itens):
    volume = models.PositiveSmallIntegerField("Volume")
    autor = models.CharField("Autor", max_length=100)
    editora = models.CharField("Editora", max_length=100)

class Filme(Itens):
    volume = models.PositiveSmallIntegerField("Volume")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

class Serie(Itens):
    qtd_temporadas = models.PositiveSmallIntegerField("Número de temporadas")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

def pre_save_itens(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(pre_save_itens, sender=Itens)