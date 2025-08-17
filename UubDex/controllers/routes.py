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
    
    @app.route("/pokemonSelected", methods=['POST', 'GET'])
    def pokemonSelected():
        return render_template("selectedPokemon.html")
    
    @app.route("items", methods=['POST', 'GET'])
    def items():
        res = getPokemonData.getItem("")
        return render_template("items.html", res=res)
    
    def itemSelected():
        return render_template("selectedItem.html")
    
    @app.route("/moves", methods=['POST', 'GET'])
    def moves():
        res = getPokemonData.getMove("")
        return render_template("moves.html", res=res)
    
    @app.route("/moveSelected", methods=['POST', 'GET'])
    def moveSelected():
        return render_template("selectedMove.html")