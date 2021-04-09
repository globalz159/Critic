from django.urls import path

from .views import filme, livro, serie

urlpatterns = [
    path('filme/<int:pk>', filme, name="filme"),
    path('livro/<int:pk>', livro, name="livro"),
    path('serie/<int:pk>', serie, name="serie"),
]
