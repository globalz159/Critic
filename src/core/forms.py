from django import forms

from .models import Usuario

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'data_nascimento', 'estado', 'cidade', 'username', 'email', 'senha']