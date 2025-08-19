import requests
# subsitua por urllib, request e json

BASE_URL = "https://pokeapi.co/api/v2/"

def search(q):    
    if q is str:
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

def getPokedex(id):
    try:
        r = requests.get(f"{BASE_URL}/pokemon-species/{id}")
        
        pokemonData = r.json()
    except Exception as e:
        pokemonData = f"Nenhuma entrada da pokédex foi encontrado: {e}"
    
    return pokemonData

def getEvolutionChain(id):
    try:

        r = requests.get(getPokedex(id)["evolution_chain"]["url"])
        evolutionData = r.json()
    except Exception as e:
        evolutionData = f"Nenhuma cadeia de evolução foi encontrada: {e}"
    
    return evolutionData


def parse_evolution_chain(chain):
    evolutions = []


    species_url = chain["species"]["url"]
    species_id = int(species_url.rstrip("/").split("/")[-1])
    evolutions.append({
        "id": species_id,
        "name": chain["species"]["name"],
        "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{species_id}.png",
    })

    for evo in chain.get("evolves_to", []):
        evolutions.extend(parse_evolution_chain(evo))

    return evolutions


def parse_moves(pokeInfo):
    moves = {
        "level-up": [],
        "machine": [],
        "egg": [],
        "tutor": []
    }

    for m in pokeInfo["moves"]:
        move_data = requests.get(m["move"]["url"]).json()
        move_type = move_data["type"]["name"]

        for vgd in m["version_group_details"]:
            if vgd["version_group"]["name"] != "sword-shield":
                continue

            method = vgd["move_learn_method"]["name"]
            move_entry = {"name": m["move"]["name"], "type": move_type}
            if method == "level-up":
                move_entry["level"] = vgd["level_learned_at"]
            if method in moves:
                moves[method].append(move_entry)

    return moves
