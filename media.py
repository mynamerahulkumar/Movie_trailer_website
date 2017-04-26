import webbrowser

class Movie():
    def __init__(movie,movie_title,movie_storyline,poster_image,trailer_youtube):
        movie.title=movie_title
        movie.storyline=movie_storyline
        movie.poster_image_url=poster_image
        movie.trailer_youtube_url=trailer_youtube
        #ABOVE ARE INITLIAZATION OF MOVIE CLASS 
    def show_trailer(movie):
        webbrowser.open(movie.trailer_youtube_url)
