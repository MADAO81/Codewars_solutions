# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python


# import math

# def what_century(year):
#     century = math.ceil(int(year)/100)
#     if 10 < century < 21:
#         ending = 'th'
#     elif century % 10 == 1:
#         ending = 'st'
#     elif century % 10 == 2:
#         ending = 'nd'
#     elif century % 10 == 3:
#         ending = 'rd'
#     else:
#         ending = 'th'
#     return str(century)+ending


def what_century(year):
    n = (int(year) - 1) // 100 + 1
    return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
