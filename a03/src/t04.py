"""

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
print("Before reversing")

for y in source:
    print(y)

print("After reversing")
source.reverse()

for x in source:
    print(x)
