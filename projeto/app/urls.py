from django.urls import path
from . import views
from .views import listar_pokemons, criar_pokemon, deletar_pokemon, atualizar_pokemon

urlpatterns = [
    path('', views.home, name='home'),
    path('listar_pokemons', listar_pokemons, name='listar_pokemons'),
    path('criar_pokemon', criar_pokemon, name='criar_pokemon'),
    path('delete/<int:pk>', deletar_pokemon, name='deletar_pokemon'),
    path('atualizar/<int:pk>', atualizar_pokemon, name='atualizar_pokemon' ),
]
