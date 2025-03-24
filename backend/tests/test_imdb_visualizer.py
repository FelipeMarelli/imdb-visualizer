import unittest

from backend.imdb_visualizer import ImdbVisualizer


class ImdbVisualizerTestCase(unittest.TestCase):
    def test_can_get_movies_information_from_an_empty_movies_file(self):
        empty_movies_file = self.create_movies_csv_file_with([])

        imdb_visualizer = ImdbVisualizer(empty_movies_file)
        all_movies_information = imdb_visualizer.get_all_movies_information()

        self.assertEqual(0, len(all_movies_information))

    def test_can_get_all_movies_information_from_a_movies_file(self):
        a_movie_csv_entry = self._titanic_movie_csv_entry()
        another_movie_csv_entry = self._nemo_movie_csv_entry()
        movies_file = self.create_movies_csv_file_with([a_movie_csv_entry, another_movie_csv_entry])

        imdb_visualizer = ImdbVisualizer(movies_file)
        all_movies_information = imdb_visualizer.get_all_movies_information()

        amount_of_loaded_movies = len(all_movies_information)
        self.assertEqual(2, amount_of_loaded_movies)

        first_loaded_movie_information = all_movies_information[0]
        expected_first_movie_information = self._titanic_movie_information()
        self.assertEqual(expected_first_movie_information, first_loaded_movie_information)

        second_loaded_movie_information = all_movies_information[1]
        expected_second_movie_information = self._nemo_movie_information()
        self.assertEqual(expected_second_movie_information, second_loaded_movie_information)

    def test_can_filter_movies_by_title(self):
        a_movie_csv_entry = self._titanic_movie_csv_entry()
        another_movie_csv_entry = self._nemo_movie_csv_entry()
        movies_file = self.create_movies_csv_file_with([a_movie_csv_entry, another_movie_csv_entry])

        imdb_visualizer = ImdbVisualizer(movies_file)
        filtered_movies = imdb_visualizer.filter_movies_by_title("nemo")

        self.assertEqual(1, len(filtered_movies))
        self.assertEqual(self._nemo_movie_information(), filtered_movies[0])

    def create_movies_csv_file_with(self, movie_entries):
        movies_csv_file = "movies.csv"
        with open(movies_csv_file, "w") as csv_file:
            csv_file.write(self._movies_file_csv_headers())
            for entry in movie_entries:
                csv_file.write(entry)

        return movies_csv_file

    def _titanic_movie_information(self):
        return {
            "imdb_title_id": "tt0000001",
            "title": "titanic",
            "original_title": "titanic original",
            "year": "1997",
            "date_published": "1997-01-01",
            "genre": "action",
            "duration": "120",
            "country": "usa",
            "language": "english",
            "director": "james cameron",
            "writer": "james cameron",
            "production_company": "20th century fox",
            "actors": "leonardo dicaprio",
            "description": "description",
            "avg_vote": "7.9",
            "votes": "1",
            "budget": "2",
            "usa_gross_income": "3",
            "worlwide_gross_income": "4",
            "metascore": "5",
            "reviews_from_users": "6",
            "reviews_from_critics": "7"
        }

    def _titanic_movie_csv_entry(self):
        return ("tt0000001,titanic,titanic original,1997,1997-01-01,action,120,usa,english,james cameron,"
                "james cameron,20th century fox,leonardo dicaprio,description,7.9,1,2,3,4,5,6,7\n")

    def _nemo_movie_information(self):
        return {
            "imdb_title_id": "tt0000002",
            "title": "nemo",
            "original_title": "nemo original",
            "year": "2003",
            "date_published": "2003-01-01",
            "genre": "animation",
            "duration": "100",
            "country": "usa",
            "language": "english",
            "director": "andrew stanton",
            "writer": "andrew stanton",
            "production_company": "pixar",
            "actors": "albert brooks",
            "description": "description",
            "avg_vote": "8.1",
            "votes": "2",
            "budget": "3",
            "usa_gross_income": "4",
            "worlwide_gross_income": "5",
            "metascore": "6",
            "reviews_from_users": "7",
            "reviews_from_critics": "8"
        }

    def _nemo_movie_csv_entry(self):
        return ("tt0000002,nemo,nemo original,2003,2003-01-01,animation,100,usa,english,andrew stanton,"
                "andrew stanton,pixar,albert brooks,description,8.1,2,3,4,5,6,7,8\n")

    def _movies_file_csv_headers(self):
        return ("imdb_title_id,title,original_title,year,date_published,genre,duration,country,language,director,"
                "writer,production_company,actors,description,avg_vote,votes,budget,usa_gross_income,"
                "worlwide_gross_income,metascore,reviews_from_users,reviews_from_critics\n")
