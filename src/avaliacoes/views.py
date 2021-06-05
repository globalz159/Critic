from django.shortcuts import render, redirect

from itens.views import item
from .forms import  AvaliarFilme, AvaliarSerie, AvaliarLivro

from .models import *
from itens.models import *
from comentarios.models import *


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
    context['url_avaliacao'] = request.get_full_path()

    if tipo_item == 'filme':
        obj_class = AvaliacaoFilme
        item_class = Filme
        comentario_class = ComentarioFilme
        obj_name = 'Filme'
        plural_obj_name = 'Filmes'
        search_params = ('titulo', 'pais', 'diretor')

    elif tipo_item == 'livro':
        obj_class = AvaliacaoLivro
        item_class = Livro
        comentario_class = ComentarioLivro
        obj_name = 'Livro'
        plural_obj_name = 'Livros'
        search_params = ('titulo', 'pais', 'autor')

    elif tipo_item == 'serie':
        obj_class = AvaliacaoSerie
        item_class = Serie
        comentario_class = ComentarioSerie
        obj_name = 'Série'
        plural_obj_name = 'Séries'
        search_params = ('titulo', 'pais', 'diretor')

    obj = obj_class.objects.get(pk=av_id)
    item_obj = item_class.objects.get(pk=item_id)

    if request.method == 'POST':
        if 'form_avaliacao' in request.POST:
            if 'curtir' in request.POST:
                obj.curtir(request.user)
            elif 'descurtir' in request.POST:
                obj.descurtir(request.user)
            elif 'comentar_action' in request.POST:
                texto_comentario = request.POST.get('comentario_field', False)
                if texto_comentario:
                    new_comentario = comentario_class(user_id=request.user, texto=texto_comentario, avaliacao=obj)
                    new_comentario.save()
                    context['new_comentario'] = new_comentario

        elif 'form_comentario' in request.POST:
            comentario = comentario_class.objects.get(pk=int(request.POST.get('comentario_id')))
            if tipo_item == 'filme':
                likes_comentario = comentario.likecomentariofilme_set.all()
            elif tipo_item == 'livro':
                likes_comentario = comentario.likecomentariolivro_set.all()
            elif tipo_item == 'serie':
                likes_comentario = comentario.likecomentarioserie_set.all()

            comentario_liked_users = []
            for like in likes_comentario:
                comentario_liked_users.append(like.user_id)

            if 'curtir' in request.POST:
                if request.user not in comentario_liked_users:
                    comentario.curtir(request.user)
                else:
                    comentario.descurtir(request.user)
            elif 'descurtir' in request.POST:
                comentario.descurtir(request.user)

    if tipo_item == 'filme':
        likes = obj.likeavaliacaofilme_set.all()
        comentarios = obj.comentariofilme_set.filter(comentario_pai=None)
    elif tipo_item == 'livro':
        likes = obj.likeavaliacaolivro_set.all()
        comentarios = obj.comentariolivro_set.filter(comentario_pai=None)
    elif tipo_item == 'serie':
        likes = obj.likeavaliacaoserie_set.all()
        comentarios = obj.comentarioserie_set.filter(comentario_pai=None)

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
        'comentarios': comentarios,
    })

    return render(request, 'avaliacao.html', context)

def avaliacoes_item(request, tipo_item, item_id):
    context = {}
    context['app_name'] = tipo_item

    if tipo_item == 'filme':
        # Classes
        av_class = AvaliacaoFilme
        item_class = Filme
        comentario_class = ComentarioFilme
        # Strings
        obj_name = 'Filme'
        plural_obj_name = 'Filmes'
        search_params = ('titulo', 'pais', 'diretor')
        # Objects
        item_obj = item_class.objects.get(pk=item_id)
        avaliacoes = item_obj.avaliacaofilme_set.all()

    elif tipo_item == 'livro':
        # Classes
        av_class = AvaliacaoLivro
        item_class = Livro
        comentario_class = ComentarioLivro
        # Strings
        obj_name = 'Livro'
        plural_obj_name = 'Livros'
        search_params = ('titulo', 'pais', 'autor')
        # Objects
        item_obj = item_class.objects.get(pk=item_id)
        avaliacoes = item_obj.avaliacaolivro_set.all()

    elif tipo_item == 'serie':
        # Classes
        av_class = AvaliacaoSerie
        item_class = Serie
        comentario_class = ComentarioSerie
        # Strings
        obj_name = 'Série'
        plural_obj_name = 'Séries'
        search_params = ('titulo', 'pais', 'diretor')
        # Objects
        item_obj = item_class.objects.get(pk=item_id)
        avaliacoes = item_obj.avaliacaoserie_set.all()


    avaliacoes = avaliacoes.order_by('create_date')

    """if request.method == 'POST':
        if 'curtir' in request.POST:
            obj.curtir(request.user)
        elif 'descurtir' in request.POST:
            obj.descurtir(request.user)
        elif 'comentar_action' in request.POST:
            texto_comentario = request.POST.get('comentario_field', False)
            if texto_comentario:
                new_comentario = comentario_class(user_id=request.user, texto=texto_comentario, avaliacao=obj)
                new_comentario.save()
                context['new_comentario'] = new_comentario"""

    context.update({
        'item_obj': item_obj,
        'obj_name': obj_name,
        'plural_obj_name': plural_obj_name,
        'search_filters': search_params,
    })

    return render(request, 'avaliacoes_item.html', context)
