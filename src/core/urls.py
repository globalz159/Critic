from django.urls import path

from .views import cadastro, index, v404, v500, carregar_cidades, livros, filmes, series

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('404', v404, name='v404'),
    path('500', v500, name='v500'),
    path('livros', livros, name='livros'),
    path('filmes', filmes, name='filmes'),
    path('series', series, name='series'),

    path('ajax/get-cidades-ajax/', carregar_cidades, name='get-cidades-ajax'),
]


