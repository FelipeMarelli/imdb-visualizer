# Estas funciones más adelante podrían ser modeladas con Factories u otros objetos más complejos.

def create_movies_csv_file_with(movie_entries):
    movies_csv_file = "movies.csv"
    with open(movies_csv_file, "w") as csv_file:
        csv_file.write(_movies_file_csv_headers())
        for entry in movie_entries:
            csv_file.write(entry)

    return movies_csv_file


def _movies_file_csv_headers():
    return ("imdb_title_id,title,original_title,year,date_published,genre,duration,country,language,director,"
            "writer,production_company,actors,description,avg_vote,votes,budget,usa_gross_income,"
            "worlwide_gross_income,metascore,reviews_from_users,reviews_from_critics\n")


def titanic_movie_information():
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


def titanic_movie_csv_entry():
    return ("tt0000001,titanic,titanic original,1997,1997-01-01,action,120,usa,english,james cameron,"
            "james cameron,20th century fox,leonardo dicaprio,description,7.9,1,2,3,4,5,6,7\n")


def nemo_movie_information():
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


def nemo_movie_csv_entry():
    return ("tt0000002,nemo,nemo original,2003,2003-01-01,animation,100,usa,english,andrew stanton,"
            "andrew stanton,pixar,albert brooks,description,8.1,2,3,4,5,6,7,8\n")
