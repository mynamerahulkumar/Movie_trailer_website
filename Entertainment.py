import media
import fresh_tomatoes

toy_story=media.Movie("Toy story","A story of a toy","http://www.dan-dare.org/FreeFun/Images/CartoonsMoviesTV/ToyStory2Wallpaper2800.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

#toy_story.show_trailer()

kabil=media.Movie("Love stroy","A blind love story","http://www.bestupdatez.com/wp-content/uploads/2016/08/New-Upcoming-Drama-Movie-Kabil-2.png",
                "https://www.youtube.com/watch?v=nubDFeiUAsI")
#print(kabil.storyline)

dangal=media.Movie("Father-Daughter story","Wrestling to prove daughter is no more then boys","http://www.lyricsted.com/wp-content/uploads/2016/12/naina-lyrics-dangal-movie-arijit-singh-song.jpg",
                "https://www.youtube.com/watch?v=x_7YlGv9u1g")

sultan=media.Movie("Wresling stroy","A wrestler life inside ring and outside ring","http://static.koimoi.com/wp-content/new-galleries/2016/07/sultan-review-news.jpg",
                "https://www.youtube.com/watch?v=wPxqcq6Byq0")

wanted=media.Movie("IPS stroy","A true IPS and proud son story","https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Wanted7.jpg/220px-Wanted7.jpg",
                "https://www.youtube.com/watch?v=I5SljKnDHwY")

limitless=media.Movie("Limitless mind stroy","A person can acces 100 percent of his mind","http://www.kaileyck.com/wp-content/uploads/2014/11/Limitless1.jpg",
                "https://www.youtube.com/watch?v=4TLppsfzQH8")
print(kabil.storyline)

movies=[toy_story,kabil,dangal,sultan,wanted,limitless]
fresh_tomatoes.open_movies_page(movies)
