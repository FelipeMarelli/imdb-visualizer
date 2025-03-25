from flask import send_from_directory


def mount_routes(flask_app, imdb_visualizer):
    @flask_app.route("/")
    def index():
        return send_from_directory(flask_app.static_folder, "index.html")

    @flask_app.route("/movies")
    def get_all_movies():
        return {"movies": imdb_visualizer.get_all_movies_information()}

    @flask_app.route("/movies/<title>")
    def get_movies_by_title(title):
        return {"movies": imdb_visualizer.filter_movies_by_title(title)}