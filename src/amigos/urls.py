from django.urls import path

# from .views import cadastro, index, v404, v500, carregar_cidades
from .views import *

urlpatterns = [
    path('', seus_amigos, name='user_amigos'),
    path('add', adicionar_amigos, name='add_amigos'),
    path('pedidos-amizade', pedidos_amizade, name='pedidos_amizade'),
]


