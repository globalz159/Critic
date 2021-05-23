from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Filme, Livro, Serie
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

from core.backend import bloquear_acesso, bloquear_acesso_admin

@bloquear_acesso
def filme(request, pk):
    filme_obj = get_object_or_404(Filme, id=pk)
    
    context = {
        'filme': filme_obj
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
    livro_obj = get_object_or_404(Livro, id=pk)

    context = {
        'livro': livro_obj
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
    serie_obj = get_object_or_404(Serie, id=pk)

    context = {
        'serie': serie_obj
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
def cadastro_filme(request):
    if str(request.method) == 'POST':
        form = CadastroFilme(request.POST, request.FILES)

        # Validando formulário
        if form.is_valid():
            form.save()
            messages.success(request, " Cadastro realizado com sucesso !")
        else:
            messages.error(request, " Campos inválidos !")
        form = CadastroFilme()
    else:
        form = CadastroFilme()

    context = {
        'form': form,
    }

    return render(request, 'cadastro_filme.html', context)  

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
    if tipo_item == 'filme':
        objects = Filme.objects.filter(ativo=False)
    elif tipo_item == 'livro':
        objects = Livro.objects.filter(ativo=False)
    elif tipo_item == 'serie':
        objects = Serie.objects.filter(ativo=False)
    
    context = {
        'objects': objects,
        'app_name': tipo_item,
    }

    return render(request, 'validar_itens.html', context)

