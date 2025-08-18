import requests
# subsitua por urllib, request e json

BASE_URL = "https://pokeapi.co/api/v2/"

def search(q):
    q = q.replace(" ", "-")
    
    result = {
    # procura por pokemon
    'pokeRes': getPokemon(q),
    # procura por item
    'itemRes' : getItem(q),
    # procura por ability
    'abilityRes' : getAbility(q),
    # procura por move
    'moveRes' : getMove(q)
    }
    
    return result
    
def getPokemon(q):
    try:
        if q:
            r = requests.get(f"{BASE_URL}/pokemon/{q}")
            pokemonData = r.json()            
        else:
            r = requests.get(f"{BASE_URL}/pokemon/")
            pokemonData = r.json()
    
    except Exception as e:
        pokemonData = f"Nenhum pokémon foi encontrado: {e}"
    
    return pokemonData 

def getItem(q):
    try:
        if q:
            r = requests.get(f"{BASE_URL}/item/{q}")
            itemData = r.json()
        else:
            r = requests.get(f"{BASE_URL}/item/")
            itemData = r.json()
        
    except Exception as e: 
        itemData = f"Nenhum item foi encontrado: {e}"
    return itemData

def getMove(q):
    try:
        if q:
            r = requests.get(f"{BASE_URL}/move/{q}")
            moveData = r.json()            
        else:
            r = requests.get(f"{BASE_URL}/move/")
            moveData = r.json()

    except Exception as e:
        moveData = f"Nenhuma ability foi encontrada: {e}"
    return moveData

def getAbility(q):
    try:
        if q:
            r = requests.get(f"{BASE_URL}/ability/{q}")
            abilityData = r.json()
        else:
            r = requests.get(f"{BASE_URL}/ability/")
            abilityData = r.json()

    except Exception as e:
        abilityData = f"Nenhuma ability foi encontrada: {e}"
    return abilityData

def getPokedéx(id):
    try:
        r = requests.get(f"{BASE_URL}/pokemon-species/{id}")
        pokemonData = r.json()
    except Exception as e:
        pokemonData = f"Nenhuma entrada da pokédex foi encontrado: {e}"
    
    return pokemonData