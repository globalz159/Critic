from .models import *
from itens.models import *

from django.contrib import messages
from django.shortcuts import render, redirect


# DECORATOR DE BLOQUEAR ACESSO !!!!
def bloquear_acesso(view_func):
    def bloquear(request, *args,**kwargs):
        if request.user.is_anonymous:
            messages.warning(request, "Acesso negado! Faça login ou crie uma conta para acessar o app")
            return redirect('/conta/login')
        return view_func(request, *args,**kwargs)
    return bloquear

def bloquear_acesso_admin(view_func):
    def bloquear(request, *args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request, "Acesso negado! Essa área é restrita apenas aos administradores do site")
            return redirect('/')
        return view_func(request, *args,**kwargs)
    return bloquear
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Cidades e estados
def adicionar_cidades():
    lista_cidades = []
    for es in ufbr.list_uf:
        estado = Estado(sigla=es)
        estado.save()
        print(f"-> {es}")

        lista_cidades = [cidade for cidade in ufbr.list_cidades(es)]
        for nome in lista_cidades:
            cidade = Cidade(estado=estado, nome=nome)
            cidade.save()
        print(lista_cidades)
        print(" ----------------------------------------------- ")

def filter_cidades(estado):
    lista_cidades = [cidade for cidade in ufbr.list_cidades(estado)]
    cont = 0
    choices_cidades = []
    for cidade in lista_cidades:
        item_cidade = CidadesChoice(estado+str(cont), cidade)
        choices_cidades.append(item_cidade)
        cont += 1
    return choices_cidades


# Busca

def obtendo_objetos(app_name):
    if app_name in ('filme', 'livro', 'serie'):
        if app_name == 'filme':
            obj_class = Filme
        elif app_name == 'livro':
            obj_class = Livro.objects.all()
        elif app_name == 'serie':
            obj_class = Serie
        objs = obj_class.objects.filter(ativo=True)
 
    elif app_name == 'usuarios':
        objs = Usuario.objects.all()
    elif app_name == 'amigos':
        objs = Usuario.objects.all()
    else:
        objs = []

    return objs

def obtendo_parametros_busca(app_name):
    if app_name == 'filme':
        search_params = ('pais', 'diretor', 'titulo')
    elif app_name == 'livro':
        search_params = ('pais', 'autor', 'titulo')
    elif app_name == 'serie':
        search_params = ('pais', 'diretor', 'titulo')
    else:
        search_params = []
    return search_params

def filtrando_objetos(app_name, objs, search, search_filter):
    # import pdb; pdb.set_trace()
    
    if app_name in ('usuarios', 'amigos'):
        objs_filtered = objs.filter(username__icontains=search)
        objs_filtered |= objs.filter(first_name__istartswith=search)

    elif app_name in ('filme', 'serie', 'livro'):
        # Filtrando objetos
        if search_filter == 'titulo':
            objs_filtered = objs.filter(titulo__icontains=search)
        elif search_filter == 'pais':
            objs_filtered = objs.filter(pais__istartswith=search)
        elif search_filter == 'diretor':
            objs_filtered = objs.filter(diretor__istartswith=search)
        elif search_filter == 'autor':
            objs_filtered = objs.filter(autor__istartswith=search)
        else:
            objs_filtered = objs
    else:
        objs_filtered = objs
    return objs_filtered
