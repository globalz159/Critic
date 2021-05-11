from django.contrib import admin

from .models import Livro, Serie, Filme, CategoriaItem

class ItemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'pais', 'ano_lancamento')

@admin.register(Filme)
class FilmeAdmin(ItemAdmin):
    list_display = ItemAdmin.list_display + ('diretor',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ItemAdmin.list_display + ('autor',)

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ItemAdmin.list_display + ('diretor',)

@admin.register(CategoriaItem)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
