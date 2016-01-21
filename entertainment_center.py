#import other files
import media
import fresh_tomatoes

#new instance of class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "November 19, 1995")

now_you_see_me = media.Movie("Now You See Me",
                             "A story about magicians going big.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA",
                             "May 21, 2013")

inception = media.Movie("Inception",
                    "A movie about the manipulation of dreams.",
                    "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                    "https://www.youtube.com/watch?v=8hP9D6kZseM",
                    "July 8, 2010")

big_hero_6 = media.Movie("Big Hero 6",
                    "A boy genius saves the world with his fluffy friend.",
                    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                    "https://www.youtube.com/watch?v=OvgyXKDXdZY",
                    "November 7, 2014")

the_force_awakens = media.Movie("The Force Awakens",
                    "A new saga about the control of the galaxy.",
                    "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                    "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                    "December 14, 2015")

the_incredibles = media.Movie("The Incredibles",
                    "A family of superheroes learns to save the world.",
                    "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                    "https://www.youtube.com/watch?v=sZwWCrFNfzQ",
                    "November 5, 2004")

#array of instances
movies = [toy_story, now_you_see_me, inception,
          big_hero_6, the_force_awakens, the_incredibles]

#uses the fresh_tomatoes file to make html
fresh_tomatoes.open_movies_page(movies)
