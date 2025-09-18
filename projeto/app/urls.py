from django.urls import path
from . import views
from .views import listar_pokemons, criar_pokemon, deletar_pokemon, atualizar_pokemon, listar_treinador, criar_treinador, deletar_treinador, atualizar_treinador

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_pokemons', listar_pokemons, name='listar_pokemons'),
    path('criar_pokemon', criar_pokemon, name='criar_pokemon'),
    path('delete/<int:pk>', deletar_pokemon, name='deletar_pokemon'),
    path('atualizar/<int:pk>', atualizar_pokemon, name='atualizar_pokemon' ),
    path('listar_treinadores', listar_treinador, name='listar_treinadores'),
    path('criar_treinador', criar_treinador, name='criar_treinador'),
    path('delete/<int:pk>', deletar_treinador, name='deletar_treinador'),
    path('atualizar/<int:pk>', atualizar_treinador, name='atualizar_treinador' ),
]
