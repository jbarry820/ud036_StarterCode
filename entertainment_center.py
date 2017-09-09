import fresh_tomatoes
import media

"""The following are instances of the class Movie"""
avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/"
    "Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

second_hand_lions = media.Movie(
    "Second Hand Lions",
    "A boy becomes a man", "https://upload.wikimedia."
    "org/wikipedia/en/thumb/6/6a"
    "/SecondhandLions.jpg/220px-SecondhandLions.jpg",
    "https://www.youtube.com/watch?v=hzElnBgsr0s")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11"
    "/School_of_Rock_Poster.jpg",
    "http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille", "A rat is chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "http://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie(
    "Hunger Games", "A really real reality show",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "http://www.youtube.com/watch?v=PbA63a7H0bo")

evan_almighty = media.Movie(
    "Evan Almighty", "A congressman builds an ark",
    "https://upload.wikimedia.org/wikipedia/en/1/14/Evan_almightymp1.jpg",
    "https://www.youtube.com/watch?v=vtJbcMJLhJss")

matrix = media.Movie(
    "The Matrix", "A great sci fi movie",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

"""The movies variable is an array of my favorite movies"""
movies = [evan_almighty, avatar, second_hand_lions,
          ratatouille, hunger_games, matrix]

"""The following line opens the web page"""
fresh_tomatoes.open_movies_page(movies)

"""The following lines print out various values of the movies"""
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
