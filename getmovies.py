from random import randint
import requests
import media
import next_movie

# API_KEY for calling API of movies api.themoviedb.org
API_KEY = '533176d577c725129bfb43067f418091'
INDEX_ERROR_CODE = 0
URL_IMAGE = 'https://image.tmdb.org/t/p/original'
URL_YOUTUBE = 'https://www.youtube.com/watch?v='
URL_REQUEST_MOVIE = "http://api.themoviedb.org/3/movie/"


# Method to get youtube url of a trailer based on his ID
def youtube(id):
    # try to check if the Movie has youtube id in KEY attribute
    try:
        # if we could get the youtube id we create a string with youtube url
        r = requests.get(URL_REQUEST_MOVIE + id + "/videos?api_key=" + API_KEY)
        youtube_key = r.json()["results"][0]["key"]
        return URL_YOUTUBE + youtube_key
    except IndexError:
        # return error code for movies without youtube id
        return INDEX_ERROR_CODE


# function to get movies receiving the number os movies wanted to return
def getMovies(number_of_movies):
    movies_list = []
    count = 0
    while count < number_of_movies:
        # try to get the movie data from service
        try:
            # create a request to get the movie info randomly
            r = requests.get(URL_REQUEST_MOVIE + str(randint(100, 1000)) + "?api_key=" + API_KEY)  # noqa
            movie = r.json()
            # call youtube method to get the Trailer url from youtube
            youtube_url = youtube(str(movie['id']))
            # if method return the youtube url and append to list
            if(youtube_url != INDEX_ERROR_CODE):
                release_date_string = movie["release_date"][:4]
                my_movie = media.Movie(movie["title"], release_date_string, movie["overview"], URL_IMAGE + movie["poster_path"], youtube_url)  # noqa
                movies_list.append(my_movie)
                # the iterator sums 1 if the movie it's valid
                count = count + 1
        except KeyError:
            # if we receive an exception the count variable doesn't change
            print('Ops, looking for another movie!')
    return movies_list
