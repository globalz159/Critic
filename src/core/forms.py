from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Usuario, Cidade, Estado

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
                self.fields[field].help_text = ''
            if field == 'cidade':
                self.fields[field].required = False
                self.fields[field].queryset = Cidade.objects.none()

        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['cidade'].queryset = Cidade.objects.filter(estado_id=estado_id).order_by('nome')
            except (ValueError, TypeError):
                print("Deu erro !")
        elif self.instance.pk:
            self.fields['cidade'].queryset = self.instance.estado.cidade_set.order_by('nome')

    
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

