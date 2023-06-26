"""

-------------------------------------------------------
"""
# Imports

from Movie import Movie
from Movie_utilities import get_by_year, read_movies

movies = open("movies.txt", "r")

lstmovies = read_movies(movies)

byyear = get_by_year(lstmovies, 1998)

for x in byyear:
    print(x)

movies.close()
