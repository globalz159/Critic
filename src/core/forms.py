from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Usuario

class UsuarioCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'data_nascimento', 'estado', 'cidade']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput
        }
        labels = {
            'username': 'Username',
        }
    
    def __init__(self, *args, **kwargs):
        super(UsuarioCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            if field in ('username','email', 'password1','password2'):
                pass #self.fields[field].help_text = ''
            if field == 'cidade':
                self.fields[field].required = False
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AlteracaoCadastro(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'data_nascimento', 'estado', 'cidade']

