# https://www.codewars.com/kata/537baa6f8f4b300b5900106c/train/python


# import math

# def circle_area(r):
#     if r <= 0.0:
#         raise ValueError()
#     return math.pi * r * r
  

def circle_area(r):
    if r <= 0:
        raise ValueError
    return 3.14*(r**2)
    
