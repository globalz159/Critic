from django.urls import path

# from .views import cadastro, index, v404, v500, carregar_cidades
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('404', v404, name='v404'),
    path('500', v500, name='v500'),

    path('minha-conta', minha_conta, name='perfil'),

    path('busca/<str:app_name>', searchbar, name='searchbar'),

    path('ajax/get-cidades-ajax/', carregar_cidades, name='get-cidades-ajax'),
]


