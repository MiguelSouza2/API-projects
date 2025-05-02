from flask import Flask

from controllers import routes
# carregando o flask na variável app
app = Flask(__name__, template_folder='views')

routes.init_app(app)

@app.route('/miguelisack')
def miguelisack():
    return render_template('miguelisack.html')
if __name__ == '__main__':
    # iniciando o servidor no localhost na porta 5000, modo de depuração ativado
    app.run(host='0.0.0.0', port=5000, debug=True)