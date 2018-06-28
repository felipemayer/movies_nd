from random import randint
import requests
import media
import next_movie


API_KEY = '533176d577c725129bfb43067f418091'

INDEX_ERROR_CODE = 0

URL_IMAGE = 'https://image.tmdb.org/t/p/original'
URL_YOUTUBE = 'https://www.youtube.com/watch?v='
URL_REQUEST_MOVIE = "http://api.themoviedb.org/3/movie/"


def youtube(id):
    try:
        r = requests.get(URL_REQUEST_MOVIE + id + "/videos?api_key=" + API_KEY)
        youtube_key = r.json()["results"][0]["key"]
        return URL_YOUTUBE + youtube_key
    except IndexError:
        return INDEX_ERROR_CODE


def getMovies(number_of_movies):
    movies_list = []
    count = 0
    while count < number_of_movies:
        try:
            r = requests.get(URL_REQUEST_MOVIE + str(randint(100, 1000)) + "?api_key=" + API_KEY)  # noqa
            movie = r.json()
            youtube_url = youtube(str(movie['id']))
            if(youtube_url != INDEX_ERROR_CODE):
                release_date_string = movie["release_date"][:4]
                my_movie = media.Movie(movie["title"], release_date_string, movie["overview"], URL_IMAGE + movie["poster_path"], youtube_url)  # noqa
                movies_list.append(my_movie)
                count = count + 1
        except KeyError:
            print('key error')
    return movies_list
