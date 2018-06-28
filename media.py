import webbrowser


class Movie():
    """Movie class with data from movie"""
    def __init__(self, title, release_date, storyline, poster, trailer):
        self.title = title
        self.release_date = release_date
        self.storyline = storyline
        self.poster_url = poster
        self.trailer_youtube_url = trailer
