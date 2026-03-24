# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python

# import re

# def calculate(strng):
#     x,y = re.findall(r'\d+',strng)
#     return int(x)-int(y) if re.search('loses',strng) else int(x)+int(y)


def calculate(s):
    x=[int(i) for i in s.split() if i.isdigit()]
    return sum(x) if 'gains' in s.split() else x[0]-x[1]
