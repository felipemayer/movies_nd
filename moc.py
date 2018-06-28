from random import randint
import requests
import media
import fresh_tomatoes


API_KEY = '533176d577c725129bfb43067f418091'

INDEX_ERROR_CODE = 0

URL_IMAGE = 'https://image.tmdb.org/t/p/original'
URL_YOUTUBE = 'https://www.youtube.com/watch?v='
URL_REQUEST_MOVIE = "http://api.themoviedb.org/3/movie/"

movies_list = []
count = 1

def youtube(id):
	try:
		r = requests.get(URL_REQUEST_MOVIE
				+ id 
				+ "/videos?api_key=" 
				+ API_KEY )
		youtube_key = r.json()["results"][0]["key"]
		
		return URL_YOUTUBE + youtube_key

	except IndexError:
		return INDEX_ERROR_CODE

while count < 11:
	try:
		r = requests.get(URL_REQUEST_MOVIE 
				+ str(randint(100, 1000))
				+"?api_key=" 
				+ API_KEY)
		movie = r.json()
		print(str(count) + " = " + movie["title"])

		youtube_url = youtube(str(movie['id']))

		print(youtube_url)

		if(youtube_url != INDEX_ERROR_CODE):
			my_movie = media.Movie(movie["title"], movie["overview"],
				URL_IMAGE + movie["poster_path"], youtube_url)
			movies_list.append(my_movie)	

			count = count + 1
	except KeyError:
		print('key error')

fresh_tomatoes.open_movies_page(movies_list)