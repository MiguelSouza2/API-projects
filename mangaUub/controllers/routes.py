from flask import render_template, request, url_for, redirect
from controllers import mangaData



def init_app(app):
    @app.route("/")
    def home():
        return render_template("index.html") 
    
    @app.route("/", methods=['GET', 'POST'])
    def searchManga():
        if request.method == 'POST':
            mangaSearch = request.form.get("search")
            if mangaSearch:
                currentManga = mangaData.getManga(mangaSearch)
                currentMangaID = currentManga['data'][0]['id']
                
                mangaChapters = mangaData.getChapters(currentMangaID)

                mangaInfo = {
                    "id" : currentManga['data'][0]['id'],
                    "title" : currentManga['data'][0]['attributes']['title']['en'],
                    "description" : currentManga['data'][0]['attributes']['description'].get("pt-br") or next(iter(currentManga['data'][0]['attributes']['description'].values()), "Sem descrição disponível"),
                    "year" : currentManga['data'][0]['attributes']['year'],
                    "tags" : currentManga['data'][0]['attributes']['tags'],
                    "status" : currentManga['data'][0]['attributes']['status'],
                    "chapters" : mangaChapters
                }
                
                
                return render_template("viewManga.html", mangaInfo=mangaInfo)
            
        
        return redirect(url_for('home'))
    
    
    # @app.route("/readManga")
    # def readManga():
        
    #     return render_template("readManga.html")

