import webbrowser


class Movie():

    """ This class provides a way to store movie related information"""

    """ This is a class variable for the class Movie"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """ This is the constructor for the class Movie"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        """ These are instance variables for the class Movie"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ This is an instance method for the class Movie"""

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
