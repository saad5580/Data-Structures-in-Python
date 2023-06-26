"""
-------------------------------------------------------
[program description]

-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies
fv = open("movies.txt", "r")

movies = read_movies(fv)

fv.close()

lst = List()

lst.insert(0, movies[0])

print("After Inserting: \n")

for x in lst:
    print(x)


print("-" * 30)

lst.append(movies[2])

print("After Appending: \n")

for x in lst:
    print(x)


lst.remove(movies[0])

print("-" * 30)

print("After removing 0th: \n")

for x in lst:
    print(x)
