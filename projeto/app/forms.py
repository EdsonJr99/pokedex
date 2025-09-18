from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome','height','weight']

class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome','idade','genero', 'main_pokemon']