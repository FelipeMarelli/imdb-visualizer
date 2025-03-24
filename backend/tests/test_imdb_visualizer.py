import unittest


class ImdbVisualizer:
    def __init__(self, movies_csv_file):
        self._movies = []
        with open(movies_csv_file, "r") as csv_file:
            is_header = True
            for line in csv_file:
                if not is_header:
                    self._movies.append(line)
                else:
                    is_header = False

    def amount_of_movies_loaded(self):
        return len(self._movies)


class ImdbVisualizerTestCase(unittest.TestCase):
    def test_can_load_an_empty_movies_file(self):
        empty_movies_file = "empty.csv"
        with open(empty_movies_file, "w") as csv_file:
            csv_file.write(self._movies_file_csv_headers())

        imdb_visualizer = ImdbVisualizer(empty_movies_file)

        self.assertEqual(0, imdb_visualizer.amount_of_movies_loaded())

    def test_can_load_one_movie_from_movies_file(self):
        one_movie_file = "one_movie.csv"
        with open(one_movie_file, "w") as csv_file:
            csv_file.write(self._movies_file_csv_headers())
            csv_file.write(self._titanic_movie_csv_entry())

        imdb_visualizer = ImdbVisualizer(one_movie_file)

        self.assertEqual(1, imdb_visualizer.amount_of_movies_loaded())

    def _titanic_movie_csv_entry(self):
        return "tt0000001,titanic,titanic original,1997,1997-01-01,action,120,usa,english,james cameron,\
            james cameron,20th century fox,leonardo dicaprio,description,7.9,1,2,3,4,5,6,7\n"

    def _movies_file_csv_headers(self):
        return "imdb_title_id,title,original_title,year,date_published,genre,duration,country,language,director,\
        writer,production_company,actors,description,avg_vote,votes,budget,usa_gross_income,worlwide_gross_income,\
        metascore,reviews_from_users,reviews_from_critics\n"
