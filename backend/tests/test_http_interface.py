import unittest

from flask import Flask

from backend.imdb_visualizer import ImdbVisualizer
from backend.routes import create_routes
from backend.tests.test_helpers import *


class InterfaceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True

        movies_file = create_movies_csv_file_with([titanic_movie_csv_entry(), nemo_movie_csv_entry()])
        imdb_visualizer = ImdbVisualizer(movies_file)
        create_routes(self.app, imdb_visualizer)

    def test_index(self):
        with self.app.test_client() as client:
            response = client.get("/")
            self.assertEqual(200, response.status_code)
            self.assertEqual("Hello, world!", response.data.decode("utf-8"))
