from django import forms

from .models import Rotas


class RotasForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Rotas
        fields = '__all__'
