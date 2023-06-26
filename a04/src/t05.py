
"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()

source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
source.insert(6)
source.insert(7)
source.insert(8)
source.insert(9)
source.insert(10)

target1, target2 = source.split_key(5)

print("Priority Queue of values greather then 5:")

for val in target1:
    print(val)

print()

print("Priority Queue of values less then 5:")


for value in target2:
    print(value)
