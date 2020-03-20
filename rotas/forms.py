from django import forms

from .models import Rotas


class RotasForm(forms.ModelForm):

    class Meta:
        model = Rotas
        fields = '__all__'
