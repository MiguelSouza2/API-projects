from flask import render_template

def init_app(app):
    # criando a primeira rota do site
    @app.route('/')

    # criando função no site
    def home():
        
        return render_template('index.html')