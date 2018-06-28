import next_movie
import getmovies

print("Getting your next movies to watch...")

# getting movie list from movies
movies_list = getmovies.getMovies(3)

# calling method to create html file and open in browser
next_movie.open_movies_page(movies_list)
