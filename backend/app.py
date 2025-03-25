from flask import Flask
from backend.imdb_visualizer import ImdbVisualizer
from backend.routes import create_routes

app = Flask(__name__)

def main():
    imdb_visualizer = ImdbVisualizer("movies.csv")
    create_routes(app, imdb_visualizer)

    app.run(host='0.0.0.0', port=8000, debug=False)
