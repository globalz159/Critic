from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import Usuario, Cidade, Estado

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

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

    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'data_nascimento', 'estado', 'cidade']

class SetPasswordForm(forms.Form):
    error_messages = {
        'wrong_password': 'A senha atual está incorreta.',
        'password_mismatch': 'As senhas digitadas não são iguais.',
    }
    new_password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Confirmação da nova senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
