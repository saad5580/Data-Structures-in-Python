
# pylint: disable=protected-access

# Imports
from BST_linked import BST


# Constants
SEP = f"\n{'-' * 60}\n"
# These VALUES match the sample BST diagram on the exam web page:
# https://bohr.wlu.ca/cp164/exam
VALUES = [11, 7, 6, 9, 8, 15, 12, 18]

print("BST_linked Testing")
print(SEP)
print("Test '_turn_right'")
print()
bst = BST()

for v in VALUES:
    bst.insert(v)
print(f"  Preorder: {bst.preorder()}")
print()
print("  Call '_turn_right'")
bst._root = bst._turn_right(bst._root)
print()
print(f"  Preorder: {bst.preorder()}")

print(SEP)
print("Test 'max_height'")
print()
bst = BST()

for v in VALUES:
    bst.insert(v)
print(f"  Preorder: {bst.preorder()}")
print()
print("  Call 'max_height'")
height = bst.max_height()
print()
print(f"  height: {height}")

print(SEP)
print("Test 'max_path'")
print()
bst = BST()

for v in VALUES:
    bst.insert(v)
print(f"  Preorder: {bst.preorder()}")
print()
print("  Call 'max_path'")
path = bst.max_path()
print()
print("  path:")

for node in path:
    print(f"{node._value}", end=", ")
print()

print(SEP)
print("Test 'flip'")
print()
bst = BST()

for v in VALUES:
    bst.insert(v)
print(f"  Preorder: {bst.preorder()}")
print()
print("  Call 'flip'")
bst.flip()
print()
print(f"  Preorder: {bst.preorder()}")

print(SEP)
