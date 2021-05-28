from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import *
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

from core.backend import bloquear_acesso, bloquear_acesso_admin
from core.models import Usuario

@bloquear_acesso
def item(request, tipo_item, pk):
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        obj_class = Filme
        obj_name = 'Filme'
        plural_obj_name = 'Filmes'
        search_params = ('titulo', 'pais', 'diretor')

    elif tipo_item == 'livro':
        obj_class = Livro
        obj_name = 'Livro'
        plural_obj_name = 'Livros'
        search_params = ('titulo', 'pais', 'autor')

    elif tipo_item == 'serie':
        obj_class = Serie
        obj_name = 'Série'
        plural_obj_name = 'Séries'
        search_params = ('titulo', 'pais', 'diretor')
    
    obj = get_object_or_404(obj_class, id=pk)

    context.update({
        'obj': obj,
        'obj_name': obj_name,
        'plural_obj_name': plural_obj_name,

        'search_filters': search_params,
    })
    return render(request, 'item.html', context)


@bloquear_acesso
def itens(request, tipo_item):
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        obj_class = Filme
        obj_name = 'Filme'
        plural_obj_name = 'Filmes'
        search_params = ('titulo', 'pais', 'diretor')

    elif tipo_item == 'livro':
        obj_class = Livro
        obj_name = 'Livro'
        plural_obj_name = 'Livros'
        search_params = ('titulo', 'pais', 'autor')

    elif tipo_item == 'serie':
        obj_class = Serie
        obj_name = 'Série'
        plural_obj_name = 'Séries'
        search_params = ('titulo', 'pais', 'diretor')

    objs = obj_class.objects.filter(ativo=True)
    
    objs_filter_recentemente = objs.order_by('data_atualizacao')
    objs_add_recentemente = []
    if objs_filter_recentemente:
        if len(objs_filter_recentemente) >=10:
            for i in range(0,9):
                objs_add_recentemente.append(objs_filter_recentemente[i])
        else:
            for i in range(0,len(objs_add_recentemente)):
                objs_add_recentemente.append(objs_filter_recentemente[i])

    context.update({
        'objs': objs,
        'objs_add_recentemente': objs_add_recentemente,
        'objs_indicados': [],

        'obj_name': obj_name,
        'plural_obj_name': plural_obj_name,

        'search_filters': search_params,
        'len_resultados': len(objs),
    })

    return render(request, 'itens.html', context)


def cadastrar_item(request, app_name):
    context = {}
    context['app_name'] = app_name
    context['categorias'] = CategoriaItem.objects.all()

    """status_message = False
    if 'status_message' in request.session:
        del request.session['status_message']"""

    if app_name == 'filme':
        form = CadastroFilme()
        obj_name = 'Filme'
    elif app_name == 'livro':
        form = CadastroLivro()
        obj_name = 'Livro'
    elif app_name == 'serie':
        form = CadastroSerie()
        obj_name = 'Série'
    else:
        return redirect('')

    context['obj_name'] = obj_name
   
    if request.method == 'POST':
        if app_name == 'filme':
            form = CadastroFilme(request.POST, request.FILES)
        elif app_name == 'livro':
            form = CadastroLivro(request.POST, request.FILES)
        elif app_name == 'serie':
            form = CadastroSerie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status_message = "Cadastro Realizado com sucesso! O item cadastrado estará disponível após um administrador validar."
            request.session['status_message'] = status_message
            return redirect(f'/itens/{app_name}')
        

    context['form'] = form


    return render(request, 'cadastro_item.html', context)


@bloquear_acesso_admin
def validar_itens(request, tipo_item):
    context = {}
    context['app_name'] = tipo_item
    
    status_message = False

    user = Usuario.objects.get(pk=request.user.id)

    if tipo_item == 'filme':
        obj_class = Filme
        obj_name = 'Filme'
    elif tipo_item == 'livro':
        obj_class = Livro
        obj_name = 'Livro'
    elif tipo_item == 'serie':
        obj_class = Serie
        obj_name = 'Série'

    if request.method == 'POST':
        using_obj = obj_class.objects.get(pk=int(request.POST.get('item_id')))
        
        if 'aprovar_cadastro' in request.POST:
            using_obj.aprovar_item(user)
            status_message = "Cadastro foi aprovado com Sucesso!"

        elif 'excluir_cadastro' in request.POST:
            using_obj.excluir_item(user)
            status_message = "Cadastro foi Excluido!"

        elif 'revisar_cadastro' in request.POST:
            using_obj.revisar_item(user)
        
        context['status_message'] = status_message

    objects = obj_class.objects.filter(ativo=False)
    
    context.update({
        'objects': objects,
        'len_objects': len(objects),
        'obj_name': obj_name,
    })

    return render(request, 'validar_itens.html', context)

