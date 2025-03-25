import unittest

from backend.app import create_flask_app
from backend.imdb_visualizer import ImdbVisualizer
from backend.tests.test_helpers import *


class InterfaceTestCase(unittest.TestCase):
    def setUp(self):
        movies_file = create_movies_csv_file_with([titanic_movie_csv_entry(), nemo_movie_csv_entry()])
        imdb_visualizer = ImdbVisualizer(movies_file)

        self.app = create_flask_app(imdb_visualizer)
        self.app.testing = True

    def test_index(self):
        """Can get the index page at '/'."""
        with self.app.test_client() as client:
            response = client.get("/")
            self.assertEqual(200, response.status_code)

    def test_get_all_movies(self):
        """Can get all movies at '/movies'."""
        with self.app.test_client() as client:
            response = client.get("/movies")
            self.assertEqual(200, response.status_code)

    def test_get_movies_by_title(self):
        """Can filter movies by name at '/movies/<title>'."""
        with self.app.test_client() as client:
            response = client.get("/movies/titanic")
            movies_json = response.json["movies"]
            self.assertEqual(200, response.status_code)
            self.assertEqual([titanic_movie_information()], movies_json)

