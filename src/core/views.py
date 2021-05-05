from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView

from django.contrib import messages

from django.contrib.auth import login, authenticate
from .forms import UsuarioCreateForm

from .models import Cidade, Estado, Usuario

from pyUFbr.baseuf import ufbr
import json

def adicionar_cidades():
    lista_cidades = []
    for es in ufbr.list_uf:
        estado = Estado(sigla=es)
        estado.save()

        lista_cidades = [cidade for cidade in ufbr.list_cidades(es)]
        for nome in lista_cidades:
            cidade = Cidade(estado=estado, nome=nome)
            cidade.save()
    return lista_cidades

def filter_cidades(estado):
    lista_cidades = [cidade for cidade in ufbr.list_cidades(estado)]
    cont = 0
    choices_cidades = []
    for cidade in lista_cidades:
        item_cidade = CidadesChoice(estado+str(cont), cidade)
        choices_cidades.append(item_cidade)
        cont += 1
    return choices_cidades

## Class Based View
class IndexView(TemplateView):
    template_name = 'index.html'

## Function Based View
def bloqueando_acesso(request):
    if request.user.is_anonymous:
        messages.warning(request, "Acesso negado! Faça login ou crie uma conta para acessar o app")
        return redirect('/conta/login')

def index(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    usuario = request.user
    print(usuario)
    
    # Botões Submit
    if request.method == 'POST':
        if 'adicionar_cidades' in request.POST:
            adicionar_cidades()
            print("Cidades adicionadas")
        elif 'view_cadastro' in request.POST:
            return redirect('/cadastro')
        elif 'do_logout' in request.POST:
            return redirect('/conta/logout')

    return render(request, 'index.html')


def cadastro(request):
    print(request.user)
    if str(request.method) == 'POST':
        form = UsuarioCreateForm(request.POST, request.FILES)
        print(form.as_p())
        # Validando formulário
        if form.is_valid():
            form.save()
            messages.success(request, " Cadastro realizado com sucesso !")
            # Redirecionando para index após o cadastro
            return redirect('/conta/login')
        else:
            error_fields = "Campos com erro: "
            for erro in form.errors:
                error_fields += erro + ', '
    else:
        form = UsuarioCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastro.html', context)

def carregar_cidades(request):
    estado_id = request.GET.get('estado')
    estado = Estado.objects.get(pk=estado_id)
    cidades = Cidade.objects.all()
    while estado == None:
        estado = request.GET.get('estado')
    print(f"Estado ID = {estado}")
    cidades = filter_cidades(estado)
    
    return render(request, 'hr/city_dropdown_list_options.html', {'cidades', cidades})

def v404(request):
    return render(request, '404.html')


def v500(request):
    return render(request, '500.html')


def adicionar_amigos(request):
    nao_amigos = [user for user in Usuario.objects.all() if user not in request.user.amigos.all() and user != request.user]

    context = {
        'nao_amigos': nao_amigos,
    }

    return render(request, 'adicionar_amigos.html', context)
