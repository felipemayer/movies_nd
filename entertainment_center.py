import fresh_tomatoes
import MoviesLocal
import MoviesApi

apiMovies = False

if (apiMovies):
    # Get Api movies
    movies_list = MoviesApi.getMovies(7)
else:
    # Get Local Json movies
    movies_list = MoviesLocal.getMovies()

fresh_tomatoes.open_movies_page(movies_list)
