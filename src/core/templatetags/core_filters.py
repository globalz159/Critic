from django import template

from ..models import Usuario, Cidade, Estado

register = template.Library()

@register.simple_tag
def get_cidade(estado):
    cidades = Cidade.objects.filter(estado=estado).order_by('nome')
    if cidades:
        return cidades
    return False