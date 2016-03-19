# A class to define the movie with four strings: title, youtube url, image url and youtube id

class Movie:
    def __init__(self, title, trailer_youtube_url, poster_image_url,trailer_youtube_id):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id
