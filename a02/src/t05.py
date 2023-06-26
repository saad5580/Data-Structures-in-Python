"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import genre_counts, read_movies


movies = open("movies.txt", "r")

lstmovies = read_movies(movies)

counts = genre_counts(lstmovies)

movies.close()

print(counts)
