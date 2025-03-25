import os
import unittest

from backend.imdb_visualizer import ImdbVisualizer
from backend.tests.test_helpers import *


class ImdbVisualizerTestCase(unittest.TestCase):
    def tearDown(self):
        os.remove("movies.csv")

    def test_can_get_all_movies_information_from_a_movies_file(self):
        a_movie_csv_entry = titanic_movie_csv_entry()
        another_movie_csv_entry = nemo_movie_csv_entry()
        movies_file = create_movies_csv_file_with([a_movie_csv_entry, another_movie_csv_entry])

        imdb_visualizer = ImdbVisualizer(movies_file)
        all_movies_information = imdb_visualizer.get_all_movies_information()

        amount_of_loaded_movies = len(all_movies_information)
        self.assertEqual(2, amount_of_loaded_movies)

        first_loaded_movie_information = all_movies_information[0]
        expected_first_movie_information = titanic_movie_information()
        self.assertEqual(expected_first_movie_information, first_loaded_movie_information)

        second_loaded_movie_information = all_movies_information[1]
        expected_second_movie_information = nemo_movie_information()
        self.assertEqual(expected_second_movie_information, second_loaded_movie_information)

    def test_can_filter_movies_by_title(self):
        a_movie_csv_entry = titanic_movie_csv_entry()
        another_movie_csv_entry = nemo_movie_csv_entry()
        movies_file = create_movies_csv_file_with([a_movie_csv_entry, another_movie_csv_entry])

        imdb_visualizer = ImdbVisualizer(movies_file)
        filtered_movies = imdb_visualizer.filter_movies_by_title("nemo")

        self.assertEqual(1, len(filtered_movies))
        self.assertEqual(nemo_movie_information(), filtered_movies[0])
