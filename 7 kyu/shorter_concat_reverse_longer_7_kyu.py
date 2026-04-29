# https://www.codewars.com/kata/54557d61126a00423b000a45/train/python


# def shorter_reverse_longer(a,b):
#     shorter = ''
#     longer = ''
#     if len(a)>=len(b):
#         shorter = b
#         longer =a
#     else:
#         shorter = a
#         longer = b
#     return shorter+''.join(reversed(longer))+shorter


def shorter_reverse_longer(a,b):
  if len(a) < len(b): a, b = b, a
  return b+a[::-1]+b
