import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializer import FavouriteSerializer
from .models import Favourites


def index(request):
    return JsonResponse({"message": "It works!"})


def getPokemons(request):

    offset = request.GET.get('offset')
    url = 'https://pokeapi.co/api/v2/pokemon/?offset={}'.format(
        offset)
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)


def getPokemon(request, id):

    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(
        id)
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['height'],
        'weight': data['weight'],
        'order': data['order'],
        'icon': data['sprites']['front_default'],
        'abilities': len(data['abilities']),
        'forms': len(data['forms']),
        'types': len(data['types']),
        'favourite': False
    }

    if Favourites.objects.filter(pk=data['id']).exists():
        pokemon['favourite'] = True
    return JsonResponse(pokemon)


@csrf_exempt
def favouritePokemons(request):
    if (request.method == "GET"):
        data = Favourites.objects.all()
        serializer = FavouriteSerializer(data, many=True)
        return JsonResponse({"message": "Success", "data": serializer.data})

    data = json.loads(request.body)
    serializer = FavouriteSerializer(data=data)

    if Favourites.objects.filter(pk=data['id']).exists():
        Favourites.objects.filter(pk=data['id']).delete()
    else:
        if (not serializer.is_valid()):
            return JsonResponse({'message': "Invalid request"}, status=400)
        serializer.save()
    return JsonResponse({"message": "Success"})
