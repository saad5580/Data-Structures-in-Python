
# pylint: disable=protected-access

# Imports
from List_linked import List


def list_print(lst):
    """
    Testing helper method.
    """
    for value in lst:
        print(value, end=", ")
    print()


# Constants
SEP = f"\n{'-' * 60}\n"
VALUES = [11, 7, 6, 9, 8, 15, 12, 18, 21]

print("List_linked Testing")
print(SEP)
print("Test 'append_list'")
print()
source = List()
target = List()

for value in VALUES:
    source.append(value)
    target.append(value)

print("  Values in source (front to rear):")
list_print(source)
print("  Values in target (front to rear):")
list_print(target)
print()
print("  Call 'append_list'")
target.append_list(source)
print()
print("  Values in source (front to rear):")
list_print(source)
print("  Values in target (front to rear):")
list_print(target)

print(SEP)
print("Test 'split_sq'")
source = List()

for value in VALUES:
    source.append(value)

print("  Values in source (front to rear):")
list_print(source)

print()
print("  Call 'split_sq'")
target1, target2 = source.split_sq()
print()
print("  Values in source (front to rear):")
list_print(source)
print("  Values in target1 (front to rear):")
list_print(target1)
print("  Values in target2 (front to rear):")
list_print(target2)
print(SEP)
print("Test randomize")
print()
source = List()
for value in VALUES:
    source.append(value)
print("  Values in source (front to rear):")
list_print(source)

print()
print("  Call 'randomize'")
target = source.randomize()
print()

print("  Values in source (front to rear):")
list_print(source)
print("  Values in target (front to rear):")
list_print(target)

print(SEP)
