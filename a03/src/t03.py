"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from Stack_array import Stack

source = Stack()

source.push(5)
source.push(7)
source.push(8)
source.push(9)
source.push(12)
source.push(14)
source.push(8)
print("Before reversing")

for y in source:
    print(y)

stack_reverse(source)

print("After reversing")
for x in source:
    print(x)
