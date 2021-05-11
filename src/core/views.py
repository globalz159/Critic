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

# DECORATOR DE BLOQUEAR ACESSO !!!!
def bloquear_acesso(view_func):
    def bloquear(request):
        if request.user.is_anonymous:
            messages.warning(request, "Acesso negado! Faça login ou crie uma conta para acessar o app")
            return redirect('/conta/login')
        return view_func(request)
    return bloquear

def bloquear_acesso_admin(view_func):
    def bloquear(request):
        if not request.user.is_superuser:
            messages.error(request, "Acesso negado! Essa área é restrita apenas aos administradores do site")
            return redirect('/')
        return view_func(request)
    return bloquear
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def adicionar_cidades():
    lista_cidades = []
    for es in ufbr.list_uf:
        estado = Estado(sigla=es)
        estado.save()
        print(f"-> {es}")

        lista_cidades = [cidade for cidade in ufbr.list_cidades(es)]
        for nome in lista_cidades:
            cidade = Cidade(estado=estado, nome=nome)
            cidade.save()
        print(lista_cidades)
        print(" ----------------------------------------------- ")

def filter_cidades(estado):
    lista_cidades = [cidade for cidade in ufbr.list_cidades(estado)]
    cont = 0
    choices_cidades = []
    for cidade in lista_cidades:
        item_cidade = CidadesChoice(estado+str(cont), cidade)
        choices_cidades.append(item_cidade)
        cont += 1
    return choices_cidades

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
def searchbar(request):
    if request.method == 'GET':
        context = {}
        objs_to_show = []

        search = request.GET.get('search', False)
        app_name = request.GET.get('select_app', 'usuario')
        users = Usuario.objects.all()
        if search:
            if app_name in ('usuario', 'amigos'):
                # Buscando objetos 
                if app_name == 'amigos':
                    users = request.user.amigos.all()
                user_filtered = users.filter(username__icontains=search)
                user_filtered |= users.filter(first_name__istartswith=search)

                list_dict = []
                user_amigos = {}
                # Obtendo amigos em comum
                for user in user_filtered:
                    amigos = user.amigos.all()
                    amigos_em_comum = [amigo for amigo in amigos if amigo in request.user.amigos.all()]
                    list_dict.append({'user': user, 'amigos_comum': amigos_em_comum, 'cont': len(amigos_em_comum)})
                    user_amigos.update({user: amigos_em_comum})
                # Ordenando por mais amigos em comum
                list_dict = sorted(list_dict, key=lambda k: k['cont'])
                # Mapeando amigos em comum com usuario
                for item in list_dict:
                    objs_to_show.append(item['user'])
                context.update({
                    'usuarios': objs_to_show, # -> List
                    'user_amigos': user_amigos, # -> Dict
                })

            elif app_name in ('filme', 'serie', 'livro'):
                # Obtendo Objetos
                if app_name == 'filme':
                    objs = Filme.objects.all()
                    search_params = ('titulo', 'pais', 'diretor')

                elif app_name == 'livro':
                    objs = Livro.objects.all()
                    search_params = ('titulo', 'pais', 'autor')

                elif app_name == 'serie':
                    objs = Serie.objects.all()
                    search_params = ('titulo', 'pais', 'diretor')

                # Filtrando objetos
                #### -- Implementar filtro de busca ---- ####
                objs_filtered = objs.filter(titulo__icontains=search)
                #objs_filtered |= objs.filter(first_name__istartswith=search)
                #### ------- ####

                for item in objs_filtered:
                    objs_to_show.append(item)

                context.update({
                    'itens': objs_to_show, # -> List
                })

            
            else:
                user_amigos = False

        else:
            user_amigos = False

        context.update({
            'search_input': search, # -> String
            'len_resultados': len(objs_to_show), # -> Int
            'app_name': app_name,
            'searching': True,
        })
        return render(request, 'busca/base_busca.html', context)

@bloquear_acesso
def seus_amigos(request):
    amigos = [user for user in Usuario.objects.all() if user in request.user.amigos.all() and user != request.user]
    app_name = 'amigos'
    context = {
        'amigos': amigos,
        'app_name': app_name,
    }
    return render(request, 'busca/base_busca.html', context)

@bloquear_acesso
def adicionar_amigos(request):
    nao_amigos = [user for user in Usuario.objects.all() if user not in request.user.amigos.all() and user != request.user]
    app_name = 'usuarios'
    context = {
        'nao_amigos': nao_amigos,
        'app_name': app_name,
    }
    return render(request, 'busca/base_busca.html', context)
