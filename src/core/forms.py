from django import forms

from .models import Usuario

class CadastroModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field == 'username':
                self.fields[field].help_text = ''

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'data_nascimento', 'estado', 'cidade', 'username', 'email', 'password']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput
        }
        labels = {
            'username': 'Nome de usuário',
        }

class LoginForm(forms.Form):
    pass
