from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Filme, Livro, Serie
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

def bloqueando_acesso(request):
    if request.user.is_anonymous:
        messages.warning(request, "Acesso negado! Faça login ou crie uma conta para acessar o app")
        return redirect('/conta/login')
    

def filme(request, pk):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    filme_obj = get_object_or_404(Filme, id=pk)
    
    context = {
        'filme': filme_obj
    }
    return render(request, 'filme.html', context)

def filmes(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

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


def livro(request, pk):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    livro_obj = get_object_or_404(Livro, id=pk)

    context = {
        'livro': livro_obj
    }
    return render(request, 'livro.html', context, name="livro")

def livros(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

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


def serie(request, pk):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    serie_obj = get_object_or_404(Serie, id=pk)

    context = {
        'serie': serie_obj
    }
    return render(request, 'serie.html', context, name="serie")

def series(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

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

def cadastro_filme(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

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

def cadastro_serie(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    if str(request.method) == 'POST':
        form = CadastroSerie(request.POST, request.FILES)

        # Validando formulário
        if form.is_valid():
            form.save()
            messages.success(request, " Cadastro realizado com sucesso !")
        else:
            messages.error(request, " Campos inválidos !")
        form = CadastroSerie()
    else:
        form = CadastroSerie()

    context = {
        'form': form,
    }

    return render(request, 'cadastro_serie.html', context)  

def cadastro_livro(request):
    bloquear = bloqueando_acesso(request)
    if bloquear:
        return bloquear

    if str(request.method) == 'POST':
        form = CadastroLivro(request.POST, request.FILES)

        # Validando formulário
        if form.is_valid():
            form.save()
            messages.success(request, " Cadastro realizado com sucesso !")
        else:
            messages.error(request, " Campos inválidos !")
        form = CadastroLivro()
    else:
        form = CadastroLivro()

    context = {
        'form': form,
    }

    return render(request, 'cadastro_livro.html', context)

def itens_a_validar(request, tipo_item):
    if tipo_item == 'filme':
        objects = Filme.objects.filter(aprovado=False)
    elif tipo_item == 'livro':
        objects = Livro.objects.filter(aprovado=False)
    elif tipo_item == 'serie':
        objects = Serie.objects.filter(aprovado=False)
    
    context = {
        'objects': objects,
    }

    return render(request, 'itens_nao_aprovados.html', context)

