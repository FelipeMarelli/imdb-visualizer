from flask import send_from_directory, request

# Mas adelante se podría modelar la interfaz HTTP con un objeto más complejo.
def mount_routes(flask_app, imdb_visualizer):
    @flask_app.route("/")
    def index():
        return send_from_directory(flask_app.static_folder, "index.html")

    @flask_app.route("/movies")
    def get_movies():
        title = request.args.get("title")
        if title:
            return {"movies": imdb_visualizer.filter_movies_by_title(title)}
        return {"movies": imdb_visualizer.get_all_movies_information()}