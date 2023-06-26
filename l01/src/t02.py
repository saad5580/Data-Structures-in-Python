"""
-------------------------------------------------------

-------------------------------------------------------
"""
from Movie import Movie

s = Movie("title", 1999, "director", 9, [0, 1, 2])
string = s.genres_list_string()
print(string)
