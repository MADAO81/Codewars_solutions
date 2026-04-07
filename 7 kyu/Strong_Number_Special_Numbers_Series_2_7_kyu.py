# https://www.codewars.com/kata/5a4d303f880385399b000001/train/python


# def strong_num(number):
#     nums = []
#     for n in str(number):
#         total = 1
#         for i in range(1,int(n)+1):
#             total *=i
#         nums.append(total)
#     if number == sum(nums):
#         return "STRONG!!!!"
#     else:
#         return "Not Strong !!"


import math

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"
