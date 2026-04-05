# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python

# import re

# def valid_ISBN10(isbn):
#     return bool(re.match("\d{9}[\dX]$", isbn)) and sum("0123456789X".index(d) * i for i, d in enumerate(isbn, 1)) % 11 == 0



def valid_ISBN10(isbn):
    # Check format
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    # Check modulo
    return sum(i*(10 if x=='X' else int(x)) for i,x in enumerate(isbn, 1)) % 11 == 0
