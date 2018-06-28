import webbrowser


class Movie():
    """docstring for Movie"""
    def __init__(self, movie_title, movie_release_date, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.release_date = movie_release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer
