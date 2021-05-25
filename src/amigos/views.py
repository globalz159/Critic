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
    status_message = False

    context['app_pedidos'] = True

    if request.method == 'POST':
        pedido_obj = PedidosAmizade.objects.get(pk=int(request.POST.get('pedido_id')))
        if 'aceitar_solicitacao' in request.POST:
            pedido_obj.aceitar_pedido()
            status_message = f"Pedido aceito com sucesso! Agora você e {pedido_obj.remetente} são amigos"
        elif 'excluir_solicitação' in request.POST:
            pedido_obj.excluir_pedido()
            status_message = f"Pedido de Amizade Recusado!"

    pedidos_enviados = request.user.remetente.filter(aceito=False)
    pedidos_recebidos = request.user.destinatario.filter(aceito=False)

    context.update({
        'len_resultados': len(pedidos_recebidos),
        'p_enviados': pedidos_enviados,
        'p_recebidos': pedidos_recebidos,
        'app_name': app_name,
        'status_message': status_message,
    })
    return render(request, 'amigos/pedidos_amizade.html', context)