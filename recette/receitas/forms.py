from django import forms
from .models import Ingrediente, Receita

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome']

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'descricao', 'ingredientes', 'instrucoes', 'equipamentos', 'porcoes']
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple(),
        }
