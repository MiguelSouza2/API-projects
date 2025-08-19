import json
from flask import render_template, request
from controllers import getPokemonData

def init_app(app):
    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/search", methods=['POST', 'GET'])
    def search():
        if request.method == 'POST':
            query = request.form.get("searchQuery")
            
            if query:
                res = getPokemonData.search(query)
                return render_template("search.html", res=res)
    
    @app.route("/pokemon", methods=['POST', 'GET'])
    def pokemon():
        res = getPokemonData.getPokemon("")
        return render_template("pokemon.html", res=res)
    
    @app.route("/selected/<id>", methods=['POST', 'GET'])
    def selected(id=None):
        if id == "pokemon":
            pokeID = request.form.get("pokeID")
            
            if pokeID:
                pokeResult = getPokemonData.search(pokeID)
                pokeInfo = pokeResult['pokeRes']
                evo_chain_data = getPokemonData.getEvolutionChain(pokeID)["chain"]
                
                pokemonData = {
                    "id" : pokeID,
                    "name" : pokeInfo["name"],
                    "description" : next(
                        (
                            entry["flavor_text"].replace("\n", " ").replace("\f", " ")
                            for entry in reversed(getPokemonData.getPokedex(pokeID)["flavor_text_entries"])
                            if entry["language"]["name"] == "en"
                        ),
                        "Description not available"
                    ),
                    "height": pokeInfo["height"],
                    "weight": pokeInfo["weight"],
                    "abilities": [a["ability"] for a in pokeInfo["abilities"] if a["is_hidden"] is False],
                    "hiddenAbilities": [a["ability"] for a in pokeInfo["abilities"] if a["is_hidden"] is True],
                    "image": pokeInfo["sprites"]["other"]["official-artwork"]["front_default"],
                    "shinyImage": pokeInfo["sprites"]["other"]["official-artwork"]["front_shiny"],
                    "stats" : {
                       "hp" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "hp")["base_stat"], 
                       "atk" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "attack")["base_stat"], 
                       "def" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "defense")["base_stat"], 
                       "spAtk" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "special-attack")["base_stat"], 
                       "spDef" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "special-defense")["base_stat"], 
                       "speed" : next(s for s in pokeInfo["stats"] if s["stat"]["name"] == "speed")["base_stat"], 
                    },
                    "evolution-chain": [
                        {
                            "id" : e["id"],
                            "name": e["species"]["name"],
                            "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{e['id']}.png",
                        }
                        for e in evo_chain_data["evolves_to"]
                    ],
                    "types" : [n for n in pokeInfo["types"]],
                    
                    # "moves" : [m["move"]["name"] for m in pokeInfo["moves"] if m["version_group_details"][0]["version_group"]["name"] == "sword-shield"],
                }
                
                return render_template("selectedPokemon.html",
                                       pokemonData=pokemonData)
        elif id == "item":
            return render_template("selectedItem.html")
        elif id == "move":
            return render_template("selectedMove.html")
        elif id == "ability":
            return render_template("selectedAbility.html")
        else:
            return render_template("index.html")

    

    
    @app.route("/items", methods=['POST', 'GET'])
    def items():
        res = getPokemonData.getItem("")
        return render_template("items.html", res=res)
    
    @app.route("/moves", methods=['POST', 'GET'])
    def moves():
        res = getPokemonData.getMove("")
        return render_template("moves.html", res=res)
    
