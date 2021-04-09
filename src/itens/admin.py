from django.contrib import admin

from .models import Livro, Serie, Filme

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pais', 'diretor', 'ano_lancamento')

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pais', 'autor', 'ano_lancamento')

class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pais', 'diretor', 'ano_lancamento')

admin.site.register(Filme, FilmeAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Serie, SerieAdmin)