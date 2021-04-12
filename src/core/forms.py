from django import forms

from .models import Usuario

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'data_nascimento', 'estado', 'cidade', 'username', 'email', 'password']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput
        }
        labels = {
            'username': 'User Name'
        }