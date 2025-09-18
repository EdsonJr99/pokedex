from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import TreinadorForm

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
        form = TreinadorForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('listar_pokemons')
    else:
        form = TreinadorForm(instance=pokemon)
    return render(request, 'criarPok.html', {'pokemon': form})

def listar_treinador(request):
    treinador = Treinador.objects.all()
    return render(request, 'listarTreins.html', {'treinador': treinador})

def criar_treinador(request):
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_treinador')
    else:
        form = TreinadorForm()
    return render(request, 'criarTrein.html', {'treinador': form})

def deletar_treinador(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listar_treinador')
    return render(request, 'confirmar_deleteTrein.html', {'treinador': treinador})

def atualizar_treinador(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('listar_treinador')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'criarTrein.html', {'pokemon': form})
