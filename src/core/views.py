from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from django.contrib.auth import login, authenticate
from .forms import UsuarioCreateForm

from .models import Cidade, Estado

from pyUFbr.baseuf import ufbr

def adicionar_cidades():
    import pdb; pdb.set_trace()
    lista_cidades = []
    for es in ufbr.list_uf:
        estado = Estado(sigla=es)
        estado.save()

        lista_cidades = [cidade for cidade in ufbr.list_cidades(es)]
        for nome in lista_cidades:
            cidade = Cidade(estado=estado, nome=nome)
            cidade.save()
    return lista_cidades

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

def index(request):
    usuario = request.user
    if usuario == "AnonymousUser":
        messages.warning(request, f"Você está logado como: '{usuario}'")
        return redirect('/login')
    print(usuario)
    if request.method == 'POST' and 'adicionar_cidades' in request.POST:
        adicionar_cidades()
        print("Cidades adicionadas")
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
    estado = None
    while estado == None:
        estado = request.GET.get('estado')
    print(f"Estado ID = {estado}")
    cidades = filter_cidades(estado)
    return render(request, 'hr/city_dropdown_list_options.html', {'cidades': cidades})

def v404(request):
    return render(request, '404.html')

def v500(request):
    return render(request, '500.html')

