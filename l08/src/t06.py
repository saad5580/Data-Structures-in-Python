"""
-------------------------------------------------------
[program description]
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import DATA1, fill_code_bst, decode_morse

bst = BST()

fill_code_bst(bst, DATA1)

text = "... --- ..."

print(decode_morse(bst, text))
