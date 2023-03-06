import requests 

POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon/'

def PokeMon(pokemon):

    pokemon = str(pokemon).strip().lower()

    print(f'Fatching Information For {pokemon}...', end="")

    Dictionary = requests.get(POKEMON_URL + pokemon)

    if Dictionary.status_code == 200:
        print('success')

        return Dictionary.json()
    else:
        print('failure')
        print(f'Dictionary : {Dictionary.status_code} ({Dictionary.reason})')
        

    return None