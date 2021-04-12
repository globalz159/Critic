from django.shortcuts import render, get_object_or_404

from .models import Filme, Livro, Serie

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


def serie(request, pk):
    serie_obj = get_object_or_404(Serie, id=pk)

    context = {
        'serie': serie_obj
    }
    return render(request, 'serie.html', context, name="serie")