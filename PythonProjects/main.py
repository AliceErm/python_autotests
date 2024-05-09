import requests 

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'dd7f5f9868cae4ccc5975be83f0c8692'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_pokemon = {
    "name": "Котикc",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_name = {
    "pokemon_id": "26604",
    "name": "NewKotik",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokeball = {
    "pokemon_id": "26604"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response.text)'''

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)