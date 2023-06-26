"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
