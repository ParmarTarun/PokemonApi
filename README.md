# Pokemon Api Wrapper

### A Simple API wrapper for [PokeAPI](https://pokeapi.co/)

### APIs:

- `GET: /api/pokemons?offset=20` => returns all pokemons with optional offset
- `GET: /api/pokemons/{id}` => returns specific formatted pokemon (with only selected & favourite attributes)
- `GET: /api/pokemons/favourites` => returns favourite pokemons from the db
- `POST: /api/pokemons/favourites` => add/remove the pokemon from the favourites list

### How to run:

- git clone
- cd into the directory
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
