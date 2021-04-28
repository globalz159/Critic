from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Cidade, Estado

from .forms import UsuarioCreateForm, AlteracaoCadastro


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    add_form = UsuarioCreateForm
    form = AlteracaoCadastro
    model = Usuario

    list_display = ('username', 'first_name', 'last_name', 'email', 'password')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'estado', 'cidade', 'amigos')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('sigla',)