# Complete the method so that it'll find the greatest product of five consecutive digits in the given string of digits.

# For example: the greatest product of five consecutive digits in the string "123834539327238239583" is 3240.

# The input string always has more than five digits.

# Adapted from Project Euler.


# def greatest_product(st):
#     result = 0
#     for i in range(len(st)+1):
#         producto = 1
#         for x in st[i:i+5]:
#             if len(st[i:i+5]) < 5 or "0" in st[i:i+5]:
#                 break
#             producto = producto *int(x)
#         if producto > result and producto !=1:
#             result = producto
#     return result

from itertools import islice
from functools import reduce

def greatest_product(n):
    numbers=[int(value) for value in n]
    result=[reduce(lambda x,y: x*y, islice(numbers, i, i+5), 1) for i in range(len(numbers)-4)]
    return max(result) 


