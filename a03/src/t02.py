"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Stack_array import Stack


source = Stack()

source.push(5)
source.push(7)
source.push(8)
source.push(9)
source.push(12)
source.push(14)
source.push(8)


print("Printing stack")
for x in source:
    print(x)

target1, target2 = source.split_alt()

print("Printing target1")

for x in target1:
    print(x)

print("Printing target2")

for y in target2:
    print(y)
