from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

from pyUFbr.baseuf import ufbr


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
        import pdb; pdb.set_trace()
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        import pdb; pdb.set_trace()
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    # PK = username
    # os campos: username, password, first_name, last_name vem de AbstractUser
    email = models.EmailField('E-mail', unique=True)
    
    estado = models.CharField("Estado", choices=choice_estados(), max_length=100)
    cidade = models.CharField("Cidade", choices=choice_cidades(), max_length=100)
    data_nascimento = models.DateField("Data de Nascimento", null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UsuarioManager()


class Cidades(models.Model):
    estado = models.CharField("Estado", max_length=2)
