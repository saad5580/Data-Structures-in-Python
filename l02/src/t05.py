"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from utilities import stack_test

file = open('food.txt', "rt")

foods = read_movies(file)

file.close()

stack_test(foods)
