"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(20)

file = open('miserables.txt', 'rt')

insert_words(file, hs)

file.close()

total, max_value = comparison_total(hs)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")
