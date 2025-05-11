from flask import render_template, request, url_for, redirect
from controllers import mangaData



def init_app(app):
    @app.route("/")
    def home():
        popularManga = mangaData.getManga()
            
        
        return render_template("index.html", popularManga=popularManga) 
    
    @app.route("/queryManga", methods=['GET', 'POST'])
    def searchManga():
        if request.method == 'POST':
            mangaSearch = request.form.get("search")
            if mangaSearch:
                mangas = mangaData.getManga(mangaSearch)
                
                return render_template("queryManga.html", mangas=mangas)

        return redirect(url_for('home'))
    
    
    @app.route("/", methods=['GET', 'POST'])
    def getManga():
        if request.method == 'POST':
            mangaId = request.form.get("manga_id")
            if mangaId:
                currentManga = mangaData.getManga(id=mangaId)
              
                mangaChapters = mangaData.getChapters(mangaId)                
                mangaInfo = {
                    "id" : currentManga['data']['id'],
                    "title" : currentManga['data']['attributes']['title']['en'],
                    "description" : currentManga['data']['attributes']['description'].get("pt-br") or next(iter(currentManga['data']['attributes']['description'].values()), "Sem descrição disponível"),
                    "year" : currentManga['data']['attributes']['year'],
                    "tags" : currentManga['data']['attributes']['tags'],
                    "status" : currentManga['data']['attributes']['status'],
                    "chapters" : mangaChapters
                }
              
              
                return render_template("viewManga.html", mangaInfo=mangaInfo)
          
      
        return redirect(url_for('home'))
    
    
    @app.route("/readManga", methods={'GET', 'POST'})
    def readManga():
        if request.method == "POST":
            chap_id = request.form.get("chapter_id")
            chap_name = request.form.get("chapter_name")
            
            if chap_id and chap_name:
                chapter_data = mangaData.getChapterImage(chap_id)
                
                chapter_images = chapter_data["chapter"]["data"]
                chapter_url = f"{chapter_data["baseUrl"]}/data/{chapter_data["chapter"]["hash"]}/"
                
                return render_template("readManga.html", chapter_url=chapter_url, chapter_images=chapter_images, chap_name=chap_name)

        return redirect(url_for('searchManga'))