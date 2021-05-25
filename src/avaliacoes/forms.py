from django import forms

from .models import AvaliacaoFilme, AvaliacaoSerie, AvaliacaoLivro
    
class AvaliarFilme(forms.ModelForm):
    class Meta:
        model = AvaliacaoFilme
        fields = ['avaliacao', 'valor', 'item', 'user_id']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            self.fields[field].help_text = '' 
               

class AvaliarSerie(forms.ModelForm):
    class Meta:
        model = AvaliacaoSerie
        fields = ['avaliacao', 'valor']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            self.fields[field].help_text = '' 

class AvaliarLivro(forms.ModelForm):
    class Meta:
        model = AvaliacaoLivro
        fields = ['avaliacao', 'valor']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = True
            self.fields[field].help_text = '' 