from django.urls import path

from .views import index, getPokemon, getPokemons, favouritePokemons

urlpatterns = [
    path("", index),
    path("pokemons/favourites", favouritePokemons),
    path("pokemons/<int:id>", getPokemon),
    path("pokemons", getPokemons)
]
