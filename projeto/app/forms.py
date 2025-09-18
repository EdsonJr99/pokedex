from django import forms
from .models import Pokemon, Treinador

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome','height','weight']

class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Treinador
        fields = ['nomeT','idade','genero', 'main_pokemon']