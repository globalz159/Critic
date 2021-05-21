from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from stdimage.models import StdImageField

from pyUFbr.baseuf import ufbr

class Estado(models.Model):
    sigla = models.CharField("Sigla", max_length=2)

    def __str__(self):
        return self.sigla
class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    nome = models.CharField("Nome", max_length=60)

    def __str__(self):
        return self.nome

def choice_cidades():
    lista_cidades = []
    for es in ufbr.list_uf:
        cont = 0
        for cidade in ufbr.list_cidades(es):
            tupla_cidade = (es+str(cont), cidade)
            lista_cidades.append(tupla_cidade)
            cont += 1
    return lista_cidades

def choice_estados():
    estados = []
    for estado in ufbr.list_uf:
        estados.append((estado, estado))
    return estados

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)
    

    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)


class Usuario(AbstractUser):
    # new_user = Usuario(username='teste', email='teste@teste.com', first_name='teste', last_name='teste', password='Teste@123')
    
    # PK = username
    # os campos: username, password, first_name, last_name vem de AbstractUser
    email = models.EmailField('E-mail', unique=True)
    imagem = StdImageField('Imagem Perfil', null=True, blank=True, upload_to='usuarios', variations={'thumbnail':(300,300)})

    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, verbose_name="Estado", null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, verbose_name="Cidade", null=True)

    data_nascimento = models.DateField("Data de Nascimento", null=True)

    amigos = models.ManyToManyField("self", db_table="Amigos", blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UsuarioManager()

    def enviar_pedido_amizade(self, destinatario_id):
        amigo_obj = Usuario.objects.get(pk=destinatario_id)
        meus_pedidos = self.remetente.all()
        if amigo_obj not in meus_pedidos.filter(destinatario=amigo_obj):
            pedido_amizade = PedidosAmizade(remetente=self, destinatario=amigo_obj)
            pedido_amizade.save()
    
    def remover_amigo(self, amigo_id):
        amigo_obj = Usuario.objects.get(pk=amigo_id)
        self.amigos.remove(amigo_obj)


class PedidosAmizade(models.Model):
    create_date = models.DateField(auto_now=True)
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='remetente')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='destinatario')
    aceito = models.BooleanField('Aceito', default=False)

    def __str__(self):
        return f'{self.remetente} -> {self.destinatario}'

    def aceitar_pedido(self):
        self.remetente.amigos.add(self.destinatario)
        self.aceito = True
    
    def recusar_pedido(self):
        self.delete()
