import webbrowser
class Movie():
    # it is used to initialise the variable
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title= movie_title
        self.storyline= movie_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube
       #this function is calling the the webbrowser to open the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
