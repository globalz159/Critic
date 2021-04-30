from django import forms

from .models import Comentario

class FormNovoComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']