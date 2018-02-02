import media

toy_story = media.Movie("Toy Story","A Story of a boy his toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")
#print (toy_story.storyline)

avatar = media.Movie("Avatar","A Marine on an aline Planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock","Using rock music to learn",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille","A rat is a Chef in Paris",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
import fresh_tomatoes
movies = [toy_story, avatar,school_of_rock,ratatouille]
#fresh_tomatoes.open_movies_page(movies)
print media.Movie.VALID_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
