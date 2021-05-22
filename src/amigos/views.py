from django.shortcuts import redirect, render

from core.views import bloquear_acesso
from core.models import *

@bloquear_acesso
def seus_amigos(request):
    context = {}
    app_name = 'amigos'
    context['app_pedidos'] = False

    amigos = [user for user in Usuario.objects.all() if user in request.user.amigos.all() and user != request.user]
    pedidos_enviados = request.user.remetente.all()
    pedidos_recebidos = request.user.destinatario.all()

    context.update({
        'amigos': amigos,
        'len_resultados': len(amigos),
        'app_name': app_name,
    })
    return render(request, 'amigos/seus_amigos.html', context)

@bloquear_acesso
def adicionar_amigos(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        search_url = request.POST.get('search_url', False)
        amigo_id = int(request.POST.get('user_id'))

        if 'add_amigo' in request.POST:
            request.user.enviar_pedido_amizade(amigo_id)
            return redirect(search_url)

    nao_amigos = [user for user in Usuario.objects.all() if user not in request.user.amigos.all() and user != request.user]
    app_name = 'usuarios'
    context = {
        'nao_amigos': nao_amigos,
        'len_resultados': len(nao_amigos),
        'app_name': app_name,
    }
    return render(request, 'busca/base_busca.html', context)

@bloquear_acesso
def pedidos_amizade(request):
    context = {}
    app_name = 'amigos'

    context['app_pedidos'] = True

    pedidos_enviados = request.user.remetente.all()
    pedidos_recebidos = request.user.destinatario.all()
    context.update({
        'p_enviados': pedidos_enviados,
        'p_recebidos': pedidos_recebidos,
        'app_name': app_name,
    })
    return render(request, 'amigos/pedidos_amizade.html', context)