from django.shortcuts import render, redirect
from .models import Pokemon, Treinador
from .forms import TreinadorForm, PokemonForm
import urllib.request
import json
from http import HTTPStatus 
from urllib.error import HTTPError

def home(request):
 try:
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace(' ','%20')
        url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
        url_pokeapi.add_header('User-Agent', 'charmander')
        
        source = urllib.request.urlopen(url_pokeapi).read()
        
        list_of_data = json.loads(source)
    
        data = {
            'number':str(list_of_data['id']),
            'name':str(list_of_data['name']).capitalize(),
            'types': ", ".join(t['type']['name'] for t in list_of_data['types']),
            'height': str(list_of_data['height']),
            'weight': str(list_of_data['weight']),
            'sprite': str(list_of_data['sprites']['front_default']),
        }
        
        print(data)
        
    else:
        data = {}
        
    return render(request, 'home.html', data)
 except HTTPError as e:
     if e.code == 404:
         return render(request, '404.html')
     

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
