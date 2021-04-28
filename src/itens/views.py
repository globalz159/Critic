from django.shortcuts import render, get_object_or_404

from .models import Filme, Livro, Serie
from .forms import CadastroFilme, CadastroSerie, CadastroLivro

def filme(request, pk):
    filme_obj = get_object_or_404(Filme, id=pk)
    
    context = {
        'filme': filme_obj
    }
    return render(request, 'filme.html', context)

def filmes(request):
    filmes = Filme.objects.all()
    
    context = {
        'filmes': filmes
    }
    return render(request, 'filme.html', context)


def livro(request, pk):
    livro_obj = get_object_or_404(Livro, id=pk)

    context = {
        'livro': livro_obj
    }
    return render(request, 'livro.html', context, name="livro")

def livros(request):
    livros = Livro.objects.all()
    
    context = {
        'livros': livros
    }
    return render(request, 'livro.html', context)    


def serie(request, pk):
    serie_obj = get_object_or_404(Serie, id=pk)

    context = {
        'serie': serie_obj
    }
    return render(request, 'serie.html', context, name="serie")

def series(request):
    series = Serie.objects.all()
    
    context = {
        'series': series
    }
    return render(request, 'serie.html', context)    

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

def cadastro_serie(request):
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

def livros(request):
    return render(request, 'livros.html')

def filmes(request):
    return render(request, 'filmes.html')

def series(request):
    return render(request, 'series.html')