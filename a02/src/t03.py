"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import get_by_genre, read_movies


movies = open("movies.txt", "r")

lstmovies = read_movies(movies)

gmovies = get_by_genre(lstmovies, 0)

movies.close()

for movie in gmovies:
    print(movie)
