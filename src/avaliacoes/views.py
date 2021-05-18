from django.shortcuts import render

def avaliar_filme(request):
    return render(request, 'avaliar_filme.html')


def avaliar_serie(request):
    return render(request, 'avaliar_serie.html')

def avaliar_livro(request):
    return render(request, 'avaliar_livro.html')    
