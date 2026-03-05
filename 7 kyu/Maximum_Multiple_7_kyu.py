# Task
# Given a Divisor and a Bound , Find the largest integer N , Such That ,
# Conditions :
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes
# The parameters (divisor, bound) passed to the function are only positive values .

# def max_multiple(divisor, bound):
#     result = 0
#     for i in range(bound+1):
#         if i % divisor == 0:
#             result = i
#     return result

def max_multiple(divisor, bound):
    return bound - (bound % divisor)
