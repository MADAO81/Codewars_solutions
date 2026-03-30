# https://www.codewars.com/kata/55d7e5aa7b619a86ed000070/train/python

# def order_word(s):
#     if s:
#         return "".join(sorted(s))
#     else:
#         return 'Invalid String!'


def order_word(s):
    return "".join(sorted(s)) if s else "Invalid String!"
