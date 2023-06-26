"""
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
ABC = "abcdefghijklmnopqrstuvwxyz"

# Task 1


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    out = ""
    for x in s:
        if x.lower() not in vowels:
            out += x
    return out


# Task 2
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    for x in fv:
        if x.isupper() == True:
            u += 1
        elif x.islower() == True:
            l += 1
        elif x.isdigit():
            d += 1
        elif x == " ":
            w += 1
        else:
            r += 1
    return u, l, d, w, r


# Task 3
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    return leap_year


# Task 4
def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(name) == 0:
        return False

    if not (name[0].isalpha() or name[0] == '_'):
        return False

    if len(name) > 1:
        for char in name[1:]:
            if not (char.isalnum() or char == '_'):
                return False

    return True

 # Task 5


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    highest = 0
    for index in range((len(a) - 1)):
        current_val = abs(a[index] - a[index + 1])
        if current_val > highest:
            highest = current_val
    return highest


# Task 6
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for index_list1 in range(len(a[0])):
        temp_list = []
        for index_main_list in range(len(a)):
            temp_list.append(a[index_main_list][index_list1])
        b.append(temp_list)
    return b


# Task 7
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    average = 0
    for lists in a:
        for value in lists:
            if value < small:
                small = value
            elif value > large:
                large = value
            total += value
            average += 1
    average = total / average
    return small, large, total, average


# Task 8
def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    for index_list1 in range(len(a[0])):
        temp_list = []
        for index_main_list in range(len(a)):
            temp_list.append(a[index_main_list][index_list1])
        b.append(temp_list)
    return b


# Task 9
def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    end = len(ABC) - 1
    estring = ""
    for x in range(len(string)):
        if string[x].lower()in ABC:
            x = ABC.index(string[x].lower())
            next_x = x + n
            if next_x <= end:
                estring += ABC[next_x - end].upper()
            else:
                pastZ = (next_x - end) - 1
                estring += ABC[pastZ].upper()
        else:
            estring += string[x]
    return estring
