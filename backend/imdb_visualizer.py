import csv

class ImdbVisualizer:
    def __init__(self, movies_csv_file):
        self._movies = []
        with open(movies_csv_file, "r", encoding="latin-1") as movies_file:
            movies_csv_reader = csv.reader(movies_file)
            next(movies_csv_reader)
            for movie_entry in movies_csv_reader:
                self._movies.append(self._parse_movie_csv_entry(movie_entry))

    def get_all_movies_information(self):
        return self._movies

    def filter_movies_by_title(self, title):
        movies_found = []
        for movie in self._movies:
            if title.lower() in movie["title"].lower():
                movies_found.append(movie)

        return movies_found

    # PRIVATE METHODS

    def _parse_movie_csv_entry(self, movie_entry):
        return {
            "imdb_title_id": movie_entry[0],
            "title": movie_entry[1],
            "original_title": movie_entry[2],
            "year": movie_entry[3],
            "date_published": movie_entry[4],
            "genre": movie_entry[5],
            "duration": movie_entry[6],
            "country": movie_entry[7],
            "language": movie_entry[8],
            "director": movie_entry[9],
            "writer": movie_entry[10],
            "production_company": movie_entry[11],
            "actors": movie_entry[12],
            "description": movie_entry[13],
            "avg_vote": movie_entry[14],
            "votes": movie_entry[15],
            "budget": movie_entry[16],
            "usa_gross_income": movie_entry[17],
            "worlwide_gross_income": movie_entry[18],
            "metascore": movie_entry[19],
            "reviews_from_users": movie_entry[20],
            "reviews_from_critics": movie_entry[21]
        }
