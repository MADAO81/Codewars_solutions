# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/train/python

# def validate(n):
#     digits = [int(x) for x in str(n)]
#     for x in range(len(digits)-2, -1, -2):
#         digits[x] = sum(map(int, str(digits[x] * 2)))
#     return sum(digits) % 10 == 0


# import numpy as np
# def validate(cc_number):
#     # split integer into array of digits
#     arr = np.array([int(i) for i in str(cc_number)])
#     # double every second digit from the right
#     arr[-2::-2] *= 2
#     # substract 9 from digits greater than 9
#     arr[arr>9] -= 9
#     # sum up all the digits and check the modulus 10
#     return np.sum(arr) % 10 == 0


def validate(n):
    digits = [int(x) for x in str(n)]
    even = [x*2 if x*2 <= 9 else x*2 - 9 for x in digits[-2::-2]]
    odd  = [x for x in digits[-1::-2]]
    return (sum(even + odd)%10) == 0
