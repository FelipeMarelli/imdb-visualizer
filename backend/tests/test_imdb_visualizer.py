import unittest


class ImdbVisualizer:
    def __init__(self, movies_csv_file):
        pass

    def amount_of_movies_loaded(self):
        return 0


class ImdbVisualizerTestCase(unittest.TestCase):
    def test_can_load_an_empty_movies_file(self):
        empty_movies_file = "empty.csv"
        with open(empty_movies_file, "w") as csv_file:
            csv_file.write(self._movies_file_csv_headers())

        imdb_visualizer = ImdbVisualizer(empty_movies_file)

        self.assertEqual(0, imdb_visualizer.amount_of_movies_loaded())

    def _movies_file_csv_headers(self):
        return "imdb_title_id,title,original_title,year,date_published,genre,duration,country,language,director,\
        writer,production_company,actors,description,avg_vote,votes,budget,usa_gross_income,worlwide_gross_income,\
        metascore,reviews_from_users,reviews_from_critics\n"
