from django.shortcuts import render
from django.contrib import messages

from .forms import CadastroModelForm

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            messages.success(request, "Cadastro realizado com sucesso !")

        else:
            messages.success(request, "Algo está errado !")

        form = CadastroModelForm()
    else:
        form = CadastroModelForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastro.html', context)
