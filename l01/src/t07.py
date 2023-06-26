"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
from Movie_utilities import read_movies
fv = open("movies.txt", "r")
movies = read_movies(fv)
fv.close()
for x in movies:
    print("-" * 30)
    print(x)
