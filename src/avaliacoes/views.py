from django.shortcuts import render, redirect
from .models import AvaliacaoFilme, AvaliacaoLivro, AvaliacaoSerie
from .forms import  AvaliarFilme, AvaliarSerie, AvaliarLivro
from itens.models import *


def avaliar_item(request, tipo_item, item_id):
    #import pdb; pdb.set_trace()    
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        obj_class = Filme
        form = AvaliarFilme()
        obj_name = 'Filme'
    elif tipo_item == 'livro':
        obj_class = Livro
        form = AvaliarLivro()
        obj_name = 'Livro'
    elif tipo_item == 'serie':
        obj_class = Serie
        form = AvaliarSerie()
        obj_name = 'Série'
   
    obj = obj_class.objects.get(pk=item_id)
    context['obj_name'] = obj_name
    context['obj'] = obj

    if request.method == 'POST':
        if tipo_item == 'filme':
            form = AvaliarFilme(request.POST, request.FILES)
        elif tipo_item == 'livro':
            form = AvaliarLivro(request.POST, request.FILES)
        elif tipo_item == 'serie':
            form = AvaliarSerie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status_message="Avaliação efetuada!"
            context['status_message'] = status_message
            request.session['status_message']= status_message
            return redirect(f"/itens/{tipo_item}/{item_id}")    

    context['form'] = form
    
    

    return render(request, 'avaliar_item.html', context)
