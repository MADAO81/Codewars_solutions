# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python

# def dup(arry):
#     result = []
#     for word in arry:
#         temp = []
#         for i,j in enumerate(word):
#             if j not in temp or j != temp[-1]:
#                 temp.append(j)
#         result.append("".join(temp))
#     return result


# import re

# def dup(arry):
#     return list(map(lambda s: re.sub(r'(\w)\1+', r'\1', s), arry))



rom itertools import groupby

def dup(arry):
    return ["".join(c for c, grouper in groupby(i)) for i in arry]
