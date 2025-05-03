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