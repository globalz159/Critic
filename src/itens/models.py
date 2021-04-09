from django.db import models

class Livro(models.Model):
    titulo = models.CharField("Título", max_length=100)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.DateField("Ano de lançamento")
    volume = models.PositiveSmallIntegerField("Volume")
    autor = models.CharField("Autor", max_length=100)
    editora = models.CharField("Editora", max_length=100)

class Filme(models.Model):
    titulo = models.CharField("Título", max_length=100)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.DateField("Ano de lançamento")
    volume = models.PositiveSmallIntegerField("Volume")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")

    """ def __init__(self, titulo, pais, ano_lancamento, diretor, volume="0", elenco=""):
        self.titulo = titulo
        self.pais = pais
        self.ano_lancamento = ano_lancamento
        self.diretor = diretor
        self.volume = volume
        self.elenco = elenco"""

class Serie(models.Model):
    titulo = models.CharField("Título", max_length=100)
    pais = models.CharField("Pais", max_length=100)
    ano_lancamento = models.DateField("Ano de lançamento")
    qtd_temporadas = models.PositiveSmallIntegerField("Número de temporadas")
    diretor = models.CharField("Diretor", max_length=100)
    elenco = models.TextField("Elenco")