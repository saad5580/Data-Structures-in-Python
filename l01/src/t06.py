"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
from Movie_utilities import read_movie
line = input(
    "Enter movie data in the format title|year|director|rating|genres: ")
movie = read_movie(line)
print(movie)
