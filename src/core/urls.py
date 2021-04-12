from django.urls import path

from .views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('', IndexView.as_view(), name='index'),
    path('cadastro', cadastro, name='cadastro')
]


