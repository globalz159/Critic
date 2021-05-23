from django.urls import path

from .views import *

urlpatterns = [
    path('filme/<int:pk>', filme, name="filme"),
    path('livro/<int:pk>', livro, name="livro"),
    path('serie/<int:pk>', serie, name="serie"),

    path('cadastro_filme', cadastro_filme, name="cadastro_filme"),
    path('cadastro_serie', cadastro_serie, name="cadastro_serie"),
    path('cadastro_livro', cadastro_livro, name="cadastro_livro"),

    path('livros', livros, name='livros'),
    path('filmes', filmes, name='filmes'),
    path('series', series, name='series'),

    path('validar_itens/<str:tipo_item>', validar_itens, name="validar_itens")

]
