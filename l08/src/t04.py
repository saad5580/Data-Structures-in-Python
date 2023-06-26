"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import DATA1, fill_code_bst


bst = BST()

fill_code_bst(bst, DATA1)

for value in bst:
    print(value.letter, value.code)
