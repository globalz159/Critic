from datetime import datetime

from django.db import models
from core.models import Usuario

from django.db.models import signals
from django.db.models.deletion import SET_NULL
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
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", null=True)
    titulo = models.CharField("Título", max_length=100, unique=True)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.IntegerField("Ano de Lançamento", default=datetime.now().year, validators=[MinValueValidator(1500), MaxValueValidator(datetime.now().year)])
    slug = models.SlugField("Slug", max_length=100, editable=False, unique=False)
    imagem = StdImageField("Imagem de capa", null=True, blank=True, upload_to='itens', variations={'thumbnail': (300, 300)})
    ativo = models.BooleanField("Ativo", default=False)
    categoria = models.ForeignKey(CategoriaItem, verbose_name="Categoria", on_delete=SET_NULL, null=True)
    tipo_item = models.CharField("Tipo", max_length=100, default='filme')

    class Meta:
        abstract = True
    
    def aprovar_item(self, user):
        if user.is_superuser:
            self.ativo = True
            self.save()
    
    def excluir_item(self, user):
        if user.is_superuser:
            self.delete()
    
    def revisar_item(self, user):
        pass

    def get_item_values(self):
        vals = {
            'titulo': self.titulo,
            'pais': self.pais,
            'ano_lancamento': self.ano_lancamento,
            'ativo': self.ativo
        }
        return vals


class Livro(Itens):
    volume = models.PositiveSmallIntegerField("Volume")
    autor = models.CharField("Autor", max_length=100)
    editora = models.CharField("Editora", max_length=100)

    def get_absolute_url(self):
        return reverse("itens:livro", kwargs={'pk': self.pk})
    
    def get_item_values(self):
        vals = super().get_item_values()
        vals.update({
            'volume': self.volume,
            'autor': self.autor,
            'editora': self.editora,
        })
        return vals

class Filme(Itens):
    volume = models.PositiveSmallIntegerField("Volume", null=True)
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:filme", kwargs={'pk': self.pk})
    
    def get_item_values(self):
        vals = super().get_item_values()
        vals.update({
            'volume': self.volume,
            'diretor': self.diretor,
            'elenco': self.elenco,
        })
        return vals

class Serie(Itens):
    qtd_temporadas = models.PositiveSmallIntegerField("Número de temporadas")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    def get_absolute_url(self):
        return reverse("itens:serie", kwargs={'pk': self.pk})
    
    def get_item_values(self):
        vals = super().get_item_values()
        vals.update({
            'qtd_temporadas': self.qtd_temporadas,
            'diretor': self.diretor,
            'elenco': self.elenco,
        })
        return vals

def pre_save_itens(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(pre_save_itens, sender=Itens)