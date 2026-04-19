# Sum of Odd Cubed Numbers
# Find the sum of the odd numbers within an array, after cubing the initial integers. 
# The function should return undefined/None/nil/NULL if any of the values aren't numbers.

# Note: Booleans should not be considered as numbers.

# def cube_odd(arr):
#     result = 0
#     for i in arr:
#         if type(i) != int:
#             return None
#         elif i % 2 != 0:
#             result += (i**3)
#     return result
    
    
def cube_odd(arr):
    return sum( n**3 for n in arr if n % 2 ) if all(type(n) == int for n in arr) else None
