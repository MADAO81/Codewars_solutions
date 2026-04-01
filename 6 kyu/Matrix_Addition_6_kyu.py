# https://www.codewars.com/kata/526233aefd4764272800036f/train/python

# def matrix_addition(a, b):
#     for row in range(len(a)):
#         for index in range(len(a)):
#             a[row][index] += b[row][index]
#     return a
  

# def matrix_addition(a, b):
#     return [[x+y for x,y in zip(first, second)] for first, second in zip(a,b)]


import numpy as np
def matrix_addition(a, b):
    return(np.mat(a)+np.mat(b)).tolist()
