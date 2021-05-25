from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Filme, Livro, Serie
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

from core.backend import bloquear_acesso, bloquear_acesso_admin
from core.models import Usuario

@bloquear_acesso
def filme(request, pk):
    app_name = 'filme'
    filme_obj = get_object_or_404(Filme, id=pk)
    
    context = {
        'filme': filme_obj, 
        'app_name':app_name
    }
    return render(request, 'filme.html', context)

@bloquear_acesso
def filmes(request):
    filmes = Filme.objects.all()
    app_name = 'filme'
    search_params = ('titulo', 'pais', 'diretor')
    
    context = {
        'filmes': filmes,
        'app_name': app_name,
        'search_filters': search_params,
        'len_resultados': len(filmes),
    }
    return render(request, 'filmes.html', context)


@bloquear_acesso
def livro(request, pk):
    app_name = 'livro'
    livro_obj = get_object_or_404(Livro, id=pk)

    context = {
        'livro': livro_obj,
        'app_name':app_name
    }
    return render(request, 'livro.html', context)

@bloquear_acesso
def livros(request):
    livros = Livro.objects.all()
    app_name = 'livro'
    search_params = ('titulo', 'pais', 'autor')
    
    context = {
        'livros': livros,
        'app_name': app_name,
        'search_filters': search_params,
        'len_resultados': len(livros),
    }
    return render(request, 'livros.html', context)    


@bloquear_acesso
def serie(request, pk):
    app_name = 'serie'
    serie_obj = get_object_or_404(Serie, id=pk)

    context = {
        'serie': serie_obj,
        'app_name':app_name
    }
    return render(request, 'serie.html', context)

@bloquear_acesso
def series(request):
    series = Serie.objects.all()
    app_name = 'serie'
    search_params = ('titulo', 'pais', 'diretor')
    
    context = {
        'series': series,
        'app_name': app_name,
        'search_filters': search_params,
        'len_resultados': len(series),
    }
    return render(request, 'series.html', context)    


@bloquear_acesso
def cadastro_confirmado(request):
    context = {}

    return render(request, 'cadastro_confirmado.html', context)  

def cadastrar_item(request, app_name):
    context = {}
    context['app_name'] = app_name

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
            return redirect('/itens/cadastro_confirmado')
        

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

