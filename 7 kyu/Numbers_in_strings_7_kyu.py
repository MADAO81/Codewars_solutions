# https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/train/python

# import re

# def solve(s:str) -> int:
#     find_numbers = re.findall(r'\d+', s)
#     numbers = list(map(int,find_numbers))
#     return max(numbers)

import re

def solve(s):
    return max(map(int,re.findall(r"(\d+)", s)))
