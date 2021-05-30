from django.shortcuts import redirect, render

from .models import *

# Create your views here.

def comentar(request, tipo_item, pk):
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        comentario_class = ComentarioFilme
    elif tipo_item == 'livro':
        comentario_class = ComentarioLivro
    elif tipo_item == 'serie':
        comentario_class = ComentarioSerie

    comentario_pai = comentario_class.objects.get(pk=pk)

    if request.method == 'POST':
        if 'comentar' in request.POST:
            texto = request.POST.get('texto')
            new = comentario_class(user_id=request.user, texto=texto, avaliacao=comentario_pai.avaliacao, comentario_pai=comentario_pai)
            new.save()
            return redirect(request.POST.get('url_avaliacao'))
        url_av = request.POST.get('url_avaliacao')

    context.update({
        'comentario_pai': comentario_pai,
        'url_avaliacao': url_av,
    })

    return render(request, 'comentar.html', context) 