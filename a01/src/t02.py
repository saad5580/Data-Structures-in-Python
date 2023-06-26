"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import file_analyze

string = open("fv.txt", "r")

u, l, d, w, r = file_analyze(string)
string.close()
print(u, l, d, w, r)
