# https://www.codewars.com/kata/57741d8f10a0a66915000001/solutions/python

# def int_diff(arr, n):
#     num=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if abs(arr[i]-arr[j])==n:
#                 num+=1
#     return num


import itertools

def int_diff(arr, n):
    return sum(abs(a-b) == n for a, b in itertools.combinations(arr, 2))
