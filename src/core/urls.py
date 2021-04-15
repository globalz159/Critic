from django.urls import path

from .views import login, cadastro, index

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro')
]


