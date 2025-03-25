from flask import Flask

from backend.imdb_visualizer import ImdbVisualizer
from backend.routes import mount_routes
from flask_cors import CORS


def create_flask_app(imdb_visualizer):
    app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
    CORS(app)
    mount_routes(app, imdb_visualizer)

    return app


def main():
    imdb_visualizer = ImdbVisualizer("IMDb_movies.csv")
    app = create_flask_app(imdb_visualizer)

    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == "__main__":
    main()
