"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies
fv = open("movies.txt", "r")

movies = read_movies(fv)

fv.close()

lst = List()

lst.append(movies[0])
lst.append(movies[1])

for value in lst:
    print(value)

index = lst.index(movies[0])

print("-" * 30)

print(f"Dellemorte Dellamore is at index {index}")

val = lst.find(movies[0])
print("-" * 30)
print("Copy of movies[0]")
print(val)
