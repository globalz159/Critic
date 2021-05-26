from django.contrib import admin

from .models import *

@admin.register(ComentarioFilme)
class ComentarioFilmeAdmin(admin.ModelAdmin):
    list_display = ('texto', 'user_id')

@admin.register(ComentarioLivro)
class ComentarioLivroAdmin(admin.ModelAdmin):
    list_display = ('texto', 'user_id')

@admin.register(ComentarioSerie)
class ComentarioSerieAdmin(admin.ModelAdmin):
    list_display = ('texto', 'user_id')