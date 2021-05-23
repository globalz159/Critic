from datetime import datetime

from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls.base import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from stdimage.models import StdImageField

class CategoriaItem(models.Model):
    categoria = models.CharField("Categoria", max_length=255)

    def __str__(self):
        return self.categoria

class Itens(models.Model):
    data_criacao = models.DateField("Data de Criação", auto_now_add=True)
    data_atualizacao = models.DateField("Data de Atualização", auto_now=True)
    titulo = models.CharField("Título", max_length=100)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.IntegerField("Ano de Lançamento", default=datetime.now().year, validators=[MinValueValidator(1500), MaxValueValidator(datetime.now().year)])
    slug = models.SlugField("Slug", max_length=100, editable=False, unique=False)
    imagem = StdImageField("Imagem de capa", null=True, blank=True, upload_to='itens', variations={'thumbnail': (300, 300)})
    ativo = models.BooleanField("Ativo", default=False)
    categoria = models.ManyToManyField(CategoriaItem, verbose_name="Categoria")

    class Meta:
        abstract = True

class Livro(Itens):
    volume = models.PositiveSmallIntegerField("Volume")
    autor = models.CharField("Autor", max_length=100)
    editora = models.CharField("Editora", max_length=100)

    def get_absolute_url(self):
        return reverse("itens:livro", kwargs={'pk': self.pk})

class Filme(Itens):
    volume = models.PositiveSmallIntegerField("Volume", null=True)
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:filme", kwargs={'pk': self.pk})

class Serie(Itens):
    qtd_temporadas = models.PositiveSmallIntegerField("Número de temporadas")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:serie", kwargs={'pk': self.pk})

def pre_save_itens(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(pre_save_itens, sender=Itens)