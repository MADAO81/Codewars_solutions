# https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python

# def factory(x):
#     def multiply_arr(arr):
#         return [num*x for num in arr]
#     return multiply_arr



# def factory(x):
#     def some(array):
#         new = []
#         for i in array:
#             new.append(i * x)
#         return new

#     return some



def factory(x):
    return lambda ar: [x*el for el in ar]
