from django.shortcuts import render, redirect
from .models import Pokemon, Treinador
from .forms import TreinadorForm, PokemonForm

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
    treinadores = Treinador.objects.all()
    return render(request, 'listarTreins.html', {'treinadores': treinadores})

def criar_treinador(request):
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_treinadores')
    else:
        form = TreinadorForm()
    return render(request, 'criarTrein.html', {'treinador': form})

def deletar_treinador(request, pk):
    treinador = Treinador.objects.get(pk=pk)
    if request.method == 'POST':
        treinador.delete()
        return redirect('listar_treinador')
    return render(request, 'confirmar_deleteTrein.html', {'treinador': treinador})

def atualizar_treinador(request, pk):
    treinador = Treinador.objects.get(pk=pk)
    if request.method == 'POST':
        form = TreinadorForm(request.POST, instance=treinador)
        if form.is_valid():
            form.save()
            return redirect('listar_treinador')
    else:
        form = TreinadorForm(instance=treinador)
    return render(request, 'criarTrein.html', {'treinador': treinador})
