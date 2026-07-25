# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python



# from math import gcd

# def solution(a):
#     return gcd(*a) * len(a)



from math import gcd
from functools import reduce

def solution(lst):
    return reduce(gcd,lst)*len(lst)
