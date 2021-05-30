from django.urls import path

from .views import *

urlpatterns = [
    path('<str:tipo_item>/<int:pk>', comentar, name='comentar'),
]