import media
import json
import fresh_tomatoes


def getMovies():
    with open('movies.json', 'r') as fp:
        movies = json.load(fp)

    movies_list = []

    for movie in movies:
        my_movie = media.Movie(movie["movie_title"], movie["movie_release_date"], movie["movie_storyline"], movie["poster_image"], movie["movie_trailer"])
        movies_list.append(my_movie)

    return movies_list
