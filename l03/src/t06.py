"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test


pq = Priority_Queue()

source = [11, 22, 55, 44, 33]

array_to_pq(pq, source)

while len(pq) > 0:
    value = pq.remove()
    print(value)
    source.append(value)

array_to_pq(pq, source)

pq_to_array(pq, source)

print(source)

file_variable = open("food.txt", "rt")

foods = read_movies(file_variable)

file_variable.close()

priority_queue_test(foods)
