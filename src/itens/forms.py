
from django import forms

from .models import Filme, Serie, Livro
    
class CadastroFilme(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'elenco', 'pais', 'ano_lancamento', 'imagem', 'categoria']

class CadastroSerie(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'diretor', 'elenco', 'pais', 'ano_lancamento', 'qtd_temporadas', 'imagem', 'categoria']   

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'volume', 'autor', 'editora', 'pais', 'ano_lancamento', 'imagem', 'categoria']                
