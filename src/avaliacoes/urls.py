from django.urls import path

from .views import *

urlpatterns = [
    path('avaliar_filme', avaliar_filme, name='avaliar_filme'),
    path('avaliar_serie', avaliar_serie, name='avaliar_serie'),
    path('avaliar_livro', avaliar_livro, name='avaliar_livro')
]