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
    
    @app.route("/selected", methods=['POST', 'GET'])
    @app.route("/selected/<id>", methods=['POST', 'GET'])
    def selected(id=None):
        if id == "pokemon":
            pokeInfo = request.form.get("pokeInfo")
            if pokeInfo:
                pokemonData = {
                    "id" : pokeInfo["id"],
                    "name" : pokeInfo["name"],
                    "description" : getPokemonData.getPokedéx(pokeInfo["id"]),
                }
                
                return render_template("selectedPokemon.html",
                                       pokeInfo=pokeInfo)
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
    
