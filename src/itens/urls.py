from django.urls import path

from .views import *

urlpatterns = [
    path('filme/<int:pk>', filme, name="filme"),
    path('livro/<int:pk>', livro, name="livro"),
    path('serie/<int:pk>', serie, name="serie"),

    path('<str:app_name>/cadastrar', cadastrar_item, name="cadastro_item"),
    path('cadastro_confirmado', cadastro_confirmado, name="cadastro_confirmado"),

    path('livros', livros, name='livros'),
    path('filmes', filmes, name='filmes'),
    path('series', series, name='series'),

    path('validar_itens/<str:tipo_item>', validar_itens, name="validar_itens"),

]
