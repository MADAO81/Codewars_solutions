# https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python

# import re

# def hydrate(s):
#     n = sum(map(int,re.findall(r'\d+',s)))
#     return f"{ n } glass{ 'es'*(n!=1) } of water"
  

def hydrate(drink_string): 
    nums = [int(i) for i in drink_string if i.isnumeric()]
    return f"{sum(nums)} glass of water" if sum(nums) == 1 else f"{sum(nums)} glasses of water" 
