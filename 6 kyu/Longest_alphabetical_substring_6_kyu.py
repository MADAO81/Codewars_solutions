# https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python

# def longest(st):
#     if len(st) <=1:
#         return st
#     longest = st[0]
#     current = st[0]
#     for i in range(1, len(st)):
#         if st[i] >= st[i-1]:
#             current += st[i]
#             if len(current) > len(longest):
#                 longest = current
#         else:
#             current = st[i]
#     return longest


import re

reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')

def longest(s):
    return max(reg.findall(s), key=len)
