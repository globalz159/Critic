from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView

from django.contrib.auth import login, authenticate
from .forms import UsuarioCreateForm

from .models import Cidade, Estado, Usuario
from itens.models import Filme, Livro, Serie

from django.db.models import Q
from django.contrib import messages
from pyUFbr.baseuf import ufbr
import json

from .backend import adicionar_cidades, filter_cidades, bloquear_acesso, bloquear_acesso_admin
from .backend import obtendo_objetos, obtendo_parametros_busca, filtrando_objetos


## Class Based View
class IndexView(TemplateView):
    template_name = 'index.html'

## Function Based View
@bloquear_acesso
def index(request):
    usuario = request.user
    print(usuario)
    # Botões Submit
    if request.method == 'POST':
        if 'adicionar_cidades' in request.POST:
            adicionar_cidades()
            print("Cidades adicionadas")
        elif 'view_cadastro' in request.POST:
            return redirect('/cadastro')
        elif 'do_logout' in request.POST:
            return redirect('/conta/logout')

    return render(request, 'index.html')


def cadastro(request):
    print(request.user)
    if str(request.method) == 'POST':
        form = UsuarioCreateForm(request.POST, request.FILES)
        print(form.as_p())
        # Validando formulário
        if form.is_valid():
            form.save()
            messages.success(request, " Cadastro realizado com sucesso !")
            # Redirecionando para index após o cadastro
            return redirect('/conta/login')
        else:
            error_fields = "Campos com erro: "
            for erro in form.errors:
                error_fields += erro + ', '
    else:
        form = UsuarioCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastro.html', context)


def carregar_cidades(request):
    estado_id = request.GET.get('estado')
    estado = Estado.objects.get(pk=estado_id)
    cidades = Cidade.objects.all()
    while estado == None:
        estado = request.GET.get('estado')
    print(f"Estado ID = {estado}")
    cidades = filter_cidades(estado)
    
    return render(request, 'hr/city_dropdown_list_options.html', {'cidades', cidades})

def v404(request):
    return render(request, '404.html')


def v500(request):
    return render(request, '500.html')


@bloquear_acesso
def searchbar(request, app_name):
    context = {}
    objs_to_show = []
    users = Usuario.objects.all()
    app_name = request.GET.get('select_app', 'usuarios')
    objs = obtendo_objetos(app_name)

    if request.method == 'GET':
        if app_name == 'amigos':
            objs = request.user.amigos.all()
        search_params = obtendo_parametros_busca(app_name)

        # import pdb; pdb.set_trace()

        # Obtendo valores da busca
        search = request.GET.get('search', False)
        context['search_input'] = search

        filtro_busca = request.GET.get('select_filter', 'titulo')
        context['search_filter'] = filtro_busca

        if search:  # Executando se a barra de busca estiver preenchida
            search_url = request.get_full_path()
            context['search_url'] = search_url

            # Filtrando objetos
            # import pdb; pdb.set_trace()
            objs_filtered = filtrando_objetos(app_name, objs, search, filtro_busca)
            
            if app_name in ('usuarios', 'amigos'):
                list_dict = []
                user_amigos = {}
                # Obtendo amigos em comum
                for user in objs_filtered:
                    amigos = user.amigos.all()
                    amigos_em_comum = [amigo for amigo in amigos if amigo in request.user.amigos.all()]
                    list_dict.append({'user': user, 'amigos_comum': amigos_em_comum, 'cont': len(amigos_em_comum)})
                    user_amigos.update({user: amigos_em_comum})
                # Ordenando por mais amigos em comum
                list_dict = sorted(list_dict, key=lambda k: k['cont'])
                # Mapeando amigos em comum com usuario
                for item in list_dict:
                    objs_to_show.append(item['user'])
                
                usuarios_solicitados = []
                for pedido in request.user.remetente.all():
                    usuarios_solicitados.append(pedido.destinatario)

                context.update({
                    'usuarios': objs_to_show, # -> List
                    'user_amigos': user_amigos, # -> Dict
                    'usuarios_solicitados': usuarios_solicitados
                })

            elif app_name in ('filme', 'serie', 'livro'):
                for item in objs_filtered:
                    objs_to_show.append(item)
                context.update({
                    'itens': objs_to_show, # -> List
                    'search_filters': search_params,
                })

        else: # Executando se a barra de busca não estiver preenchida
            if app_name in ('filme', 'livro', 'serie'):
                if app_name == 'filme':
                    context['filmes'] = objs
                elif app_name == 'livro':
                    context['livros'] = objs
                elif app_name == 'serie':
                    context['filmes'] = objs
                context['search_filters'] = search_params
                return redirect(f'/itens/{app_name}s')

    # Atualizando contexto
    context.update({
        'objs': objs_to_show,
        'len_resultados': len(objs_to_show), # -> Int
        'app_name': app_name,
        'searching': True,
    })
    return render(request, 'busca/base_busca.html', context)


def minha_conta(request):
    user = request.user
    av_filmes = user.avaliacaofilme_set.all()
    av_livros = user.avaliacaolivro_set.all()
    av_series = user.avaliacaoserie_set.all()

    avaliacoes = av_filmes.union(av_livros)
    avaliacoes = avaliacoes.union(av_series)
    avaliacoes = avaliacoes.order_by('data_criacao')
    
    context = {
        'user': user,
        'avaliacoes':avaliacoes,
    }
    return render(request, 'minha_conta.html', context)