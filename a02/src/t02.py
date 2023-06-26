"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import get_by_rating, read_movies


movies = open("movies.txt", "r")

lstmovies = read_movies(movies)

rmovies = get_by_rating(lstmovies, 8.0)

movies.close()

for movie in rmovies:
    print(movie)
