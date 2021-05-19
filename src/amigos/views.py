from django.shortcuts import render

from core.views import bloquear_acesso
from core.models import *

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
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        if 'add_amigo' in request.POST:
            amigo_id = int(request.POST.get('user_id'))
            amigo_obj = Usuario.objects.get(pk=amigo_id)
            pedido_amizade = PedidosAmizade(remetente=request.user, destinatario=amigo_obj)
            pedido_amizade.save()

    nao_amigos = [user for user in Usuario.objects.all() if user not in request.user.amigos.all() and user != request.user]
    app_name = 'usuarios'
    context = {
        'nao_amigos': nao_amigos,
        'app_name': app_name,
    }
    return render(request, 'busca/base_busca.html', context)

@bloquear_acesso
def pedidos_amizade(request):
    pedidos_enviados = request.user.remetente.all()
    pedidos_recebidos = request.user.destinatario.all()
    nao_amigos = [user for user in Usuario.objects.all() if user not in request.user.amigos.all() and user != request.user]
    app_name = 'usuarios'
    context = {
        'p_enviados': pedidos_enviados,
        'p_recebidos': pedidos_recebidos,
        'nao_amigos': nao_amigos,
        'app_name': app_name,
    }
    return render(request, 'busca/base_busca.html', context)