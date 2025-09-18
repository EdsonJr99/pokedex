from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

def home(request):
    return render(request, 'home.html')

def listar_pokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'listarPok.html', {'pokemons': pokemons})

def criar_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pokemons')
    else:
        form = PokemonForm()
    return render(request, 'criarPok.html', {'pokemon': form})

def deletar_pokemon(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listar_pokemons')
    return render(request, 'confirmar_delete.html', {'pokemon': pokemon})

def atualizar_pokemon(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('listar_pokemons')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'criarPok.html', {'pokemon': form})
