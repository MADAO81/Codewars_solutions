# Magic Sum of 3s
# The magic sum of 3s is calculated on an array by summing up odd numbers which include the digit 3.

# Complete the function which accepts an array of integers and returns its magic sum of 3s.

# Example: [3, 12, 5, 8, 30, 13] results in 16 (3 + 13)

# If there is no such number in the array, 0 should be returned.


# def magic_sum(arr):
#     digit = 3
#     op_arr = []
#     for i in arr:
#         if i % 2 != 0 and str(digit) in str(i):
#             op_arr.append(i)
#     return sum(op_arr)


def magic_sum(arr):
    return arr and sum(x for x in arr if x%2 and '3' in str(x)) or 0
