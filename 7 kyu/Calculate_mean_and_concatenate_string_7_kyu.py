# https://www.codewars.com/kata/56f7493f5d7c12d1690000b6/train/python

# def mean(lst):
#     nums = []
#     chars = []
#     for i in lst:
#         if i.isdigit():
#             nums.append(int(i))
#         else:
#             chars.append(i)
#     mean = sum(nums)/len(nums)
#     str = ''.join(chars)
#     return [float(mean),str]


def mean(lst):
    return [sum(int(n) for n in lst if n.isdigit()) / 10.0, "".join(c for c in lst if c.isalpha())]
