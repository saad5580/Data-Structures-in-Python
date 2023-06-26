"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

year = int(input("Enter year: "))

leap_year = is_leap_year(year)

if leap_year:
    print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year')
