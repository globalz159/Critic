from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from django.contrib.auth import login, authenticate
from .forms import UsuarioCreateForm

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
    print(dir(usuario))
    
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
            error_fields = "Campos "
            for erro in form.errors:
                error_fields += erro + ', '
            messages.error(request, f"{error_fields} inválidos !")
        form = UsuarioCreateForm()
    else:
        form = UsuarioCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastro.html', context)

