from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run('localhost', 3000, debug=True)