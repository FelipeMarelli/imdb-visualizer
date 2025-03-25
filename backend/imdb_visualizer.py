class ImdbVisualizer:
    def __init__(self, movies_csv_file):
        self._movies = []
        with open(movies_csv_file, "r", encoding="latin-1") as movies_file:
            _csv_headers = movies_file.readline()
            for movie_entry in movies_file:
                movie_information = self._parse_movie_csv_entry(movie_entry)
                self._movies.append(movie_information)

    def get_all_movies_information(self):
        return self._movies

    def _parse_movie_csv_entry(self, movie_entry):
        movie_entry_without_newline = movie_entry.strip()
        movie_entry_columns = movie_entry_without_newline.split(",")
        return {
            "imdb_title_id": movie_entry_columns[0],
            "title": movie_entry_columns[1],
            "original_title": movie_entry_columns[2],
            "year": movie_entry_columns[3],
            "date_published": movie_entry_columns[4],
            "genre": movie_entry_columns[5],
            "duration": movie_entry_columns[6],
            "country": movie_entry_columns[7],
            "language": movie_entry_columns[8],
            "director": movie_entry_columns[9],
            "writer": movie_entry_columns[10],
            "production_company": movie_entry_columns[11],
            "actors": movie_entry_columns[12],
            "description": movie_entry_columns[13],
            "avg_vote": movie_entry_columns[14],
            "votes": movie_entry_columns[15],
            "budget": movie_entry_columns[16],
            "usa_gross_income": movie_entry_columns[17],
            "worlwide_gross_income": movie_entry_columns[18],
            "metascore": movie_entry_columns[19],
            "reviews_from_users": movie_entry_columns[20],
            "reviews_from_critics": movie_entry_columns[21]
        }

    def filter_movies_by_title(self, title):
        movies_found = []
        for movie in self._movies:
            if title.lower() in movie["title"].lower():
                movies_found.append(movie)

        return movies_found
