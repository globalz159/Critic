from django.urls import path

from .views import *

urlpatterns = [
    path('<str:tipo_item>/<int:pk>', item, name="item"),
    path('<str:tipo_item>/', itens, name='itens'),

    path('<str:app_name>/cadastrar', cadastrar_item, name="cadastro_item"),

    path('validar_itens/<str:tipo_item>', validar_itens, name="validar_itens"),
]
