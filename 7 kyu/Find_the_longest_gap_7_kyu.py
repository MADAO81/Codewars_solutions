# https://www.codewars.com/kata/55b86beb1417eab500000051/train/python

# def gap(num):
#     binary_string = bin(num)[2:].strip('0')
#     return max((len(s) for s in binary_string.split('1')), default = 0)


# import re

# def gap(num):
#     num = bin(num)[2:]
#     return max(map(len, re.findall("(?<=1)0+(?=1)", num)), default=0)


def gap(num):
    s = bin(num)[2:].strip("0")
    return max(map(len, s.split("1")))
