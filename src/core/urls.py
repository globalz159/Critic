from django.urls import path

from .views import index, cadastro

urlpatterns = [
    path('', index),
    path('cadastro', cadastro)
]
