# https://www.codewars.com/kata/5516ab668915478845000780/train/python

# def reverse_by_center(s):
#     mid = len(s)//2
#     if len(s)%2 == 0:
#         return s[mid:] + s[:mid]
#     return s[mid +1:] + s[mid] + s[:mid]


def reverse_by_center(s):
  n=len(s)//2
  return s[-n:]+s[n:-n]+s[:n]
