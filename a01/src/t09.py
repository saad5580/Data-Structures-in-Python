"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import shift
# Put the right name, I don't remember what name it was xD
file = open("pelee.txt", "r")
new_file = open("shift.txt", "w")  # again, put the right name
string = file.read()
n = int(input("Input the shift"))  # for the n that you need in the function

newstring = shift(string, n)
new_file.write(newstring)
file.close()
new_file.close()
