# https://www.codewars.com/kata/602db3215c22df000e8544f0/train/python

# def two_are_positive(a, b, c):
#     count = 0
#     nums = [a,b,c]
#     for number in nums:
#         if number >0:
#             count +=1
#     return count == 2


def two_are_positive(a, b, c):
    return sum([a>0, b>0, c>0]) == 2
