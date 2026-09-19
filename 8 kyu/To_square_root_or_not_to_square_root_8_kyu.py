# To square(root) or not to square(root)
# Write a method, that will get an integer array as parameter and will process every number from this array.

# Return a new array with processing every number of the input-array like this:

# If the number has an integer square root, take this, otherwise square the number.

# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# Notes
# The input array will always contain only positive numbers, and will never be empty or null.




# def square_or_square_root(arr):
#     result = []
#     for x in arr:
#         root = x**0.5
#         if root.is_integer():
#             result.append(root)
#         else:
#             result.append(x*x)
#     return result


import math

def is_integer_sqrt(number):
    if number < 0:
        return False
    sqrt_value = math.sqrt(number)
    return sqrt_value % 1 == 0

def square_or_square_root(arr):
    new_arr =[]
    for i in arr:
        if is_integer_sqrt(i) == True:
            new_arr.append(i**0.5)
        else:
            new_arr.append(i**2)
    return new_arr
