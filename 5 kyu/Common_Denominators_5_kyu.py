# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python

# def convertFracts(lst):
#     if not lst:
#         return lst
    
#     from functools import reduce
#     dens = []
#     for num, den in lst:
#         dens.append(den)
#     lcd = reduce(lcm, dens)
#     lst = [[lcd * num // den, lcd] for num, den in lst]
#     return lst
    
# def gcd(a, b):
#     while b:      
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)



# from fractions import gcd
# def convertFracts(lst):
#     D = 1
#     for _,d in lst:
#         D*= d//gcd(d,D)
#     return [[D*n//d,D] for n,d in lst]




import math
import functools

def convertFracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))
