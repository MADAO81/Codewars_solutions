# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

# from math import comb
# def easyline(n):
#     return comb(2*n, n)

def easyline(n):
    return easyline(n-1)*(4*n-2)//n if n else 1
