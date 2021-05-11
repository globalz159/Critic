from django.contrib import admin

from .models import AvaliacaoFilme, AvaliacaoLivro, AvaliacaoSerie


@admin.register(AvaliacaoFilme)
class AvaliacaoFilme(admin.ModelAdmin):
    list_display = ('valor', 'user_id', 'item')

@admin.register(AvaliacaoLivro)
class AvaliacaoFilme(admin.ModelAdmin):
    list_display = ('valor', 'user_id', 'item')

@admin.register(AvaliacaoSerie)
class AvaliacaoFilme(admin.ModelAdmin):
    list_display = ('valor', 'user_id', 'item')