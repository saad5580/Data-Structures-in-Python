"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from utilities import list_test
fv = open("movies.txt", "r")

movies = read_movies(fv)

fv.close()

list_test(movies)
