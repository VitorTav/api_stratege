import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"
poke_list = list()

while url is not None:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        url = data["next"]  

        for item in data["results"]:
            pokename = item["name"]
            url_pokemons = f"https://pokeapi.co/api/v2/pokemon/{pokename}"

            response_pokemon = requests.get(url_pokemons)
            if response_pokemon.status_code == 200:
                pokemon_data = response_pokemon.json()

                infos = {
                    "name": pokename,
                    "id": pokemon_data["id"],
                    "height": pokemon_data["height"],
                    "weight": pokemon_data["weight"],
                    "is_default": pokemon_data["is_default"]
                }
                poke_list.append(infos)

                print(f"Pokémon ID: {pokemon_data['id']}")
            else:
                print(f"Erro ao obter dados para o Pokémon {pokename}")

    else:
        print(f"Erro na requisição da lista de Pokémon: {response.status_code}")
        url = None  

print(poke_list)


file_path = "C:\\Github\\pokemons.json"

with open(file_path, "w") as outfile:
    print(f"Salvando arquivo em: {file_path}")
    json.dump(poke_list, outfile, indent=4)


outfile.close()

 
