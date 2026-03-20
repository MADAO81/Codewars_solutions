# https://www.codewars.com/kata/59b401e24f98a813f9000026/train/python


# def compute_depth(n):
#     result = set()
#     for i in range(1,100):
#         result |=set(str(n*i))
#         if len(result) == 10:
#             return i



def compute_depth(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i
