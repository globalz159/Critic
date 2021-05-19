from .models import *
from core.models import *

def adicionar_amigo(id_amigo):
    amigo = Usuario.objects.all().get(pk=id_amigo)
