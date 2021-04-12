from django.urls import path

from .views import IndexView, cadastro

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro', cadastro, name='cadastro')
]


