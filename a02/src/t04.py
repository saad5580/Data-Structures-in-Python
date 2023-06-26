"""
-------------------------------------------------------

-------------------------------------------------------
"""
from Movie import Movie
from Movie_utilities import get_by_genres, read_movies


movies = open("movies.txt", "r")

lstmovies = read_movies(movies)

gmovies = get_by_genres(lstmovies, [3, 4, 5, 8])

movies.close()

for movie in gmovies:
    print(movie)
