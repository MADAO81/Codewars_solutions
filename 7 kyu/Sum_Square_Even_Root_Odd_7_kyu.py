# https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python

# from math import sqrt

# def sum_square_even_root_odd(nums):
#     sum_nums = 0
#     for i in nums:
#         if i%2 == 0:
#             sum_nums += pow(i,2)
#         else:
#             sum_nums += sqrt(i)
            
#     return round(sum_nums, 2)



def sum_square_even_root_odd(nums):
    return round(sum(n ** 2 if n % 2 == 0 else n ** 0.5 for n in nums), 2)
