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
        """Can get the index '/' page."""
        with self.app.test_client() as client:
            response = client.get("/")
            self.assertEqual(200, response.status_code)
