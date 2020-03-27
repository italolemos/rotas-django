from django import forms

from .models import Rotas


class RotasForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': "input"}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 5}))
    tamanho = forms.CharField(widget=forms.TextInput(attrs={'class': "input"}))

    class Meta:
        model = Rotas
        fields = '__all__'
