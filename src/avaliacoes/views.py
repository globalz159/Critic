from django.shortcuts import render, redirect

from itens.views import item
from .forms import  AvaliarFilme, AvaliarSerie, AvaliarLivro

from .models import *
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


def avaliacao(request, tipo_item, item_id, av_id):
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        obj_class = AvaliacaoFilme
        item_class = Filme
        like_class = LikeAvaliacaoFilme
        obj_name = 'Filme'
        plural_obj_name = 'Filmes'
        search_params = ('titulo', 'pais', 'diretor')

    elif tipo_item == 'livro':
        obj_class = AvaliacaoLivro
        item_class = Livro
        like_class = LikeAvaliacaoLivro
        obj_name = 'Livro'
        plural_obj_name = 'Livros'
        search_params = ('titulo', 'pais', 'autor')

    elif tipo_item == 'serie':
        obj_class = AvaliacaoSerie
        item_class = Serie
        like_class = LikeAvaliacaoSerie
        obj_name = 'Série'
        plural_obj_name = 'Séries'
        search_params = ('titulo', 'pais', 'diretor')

    obj = obj_class.objects.get(pk=av_id)
    item_obj = item_class.objects.get(pk=item_id)

    if tipo_item == 'filme':
        likes = obj.likeavaliacaofilme_set.all()
    elif tipo_item == 'livro':
        likes = obj.likeavaliacaolivro_set.all()
    elif tipo_item == 'serie':
        likes = obj.likeavaliacaoserie_set.all()

    if request.method == 'POST':
        if 'curtir' in request.POST:
            obj.curtir(request.user)
        elif 'descurtir' in request.POST:
            obj.descurtir(request.user)
        elif 'comentar' in request.POST:
            obj.comentar()

    liked_users = []
    for like in likes:
        liked_users.append(like.user_id)

    context.update({
        'obj': obj,
        'item_obj': item_obj,
        'obj_name': obj_name,
        'plural_obj_name': plural_obj_name,
        'search_filters': search_params,
        'liked_users': liked_users,
    })

    return render(request, 'avaliacao.html', context)
