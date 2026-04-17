# https://www.codewars.com/kata/522551eee9abb932420004a0/train/python

# def nth_fib(n):
#     if n<2:
#         return 0
#     elif n == 2:
#         return 1
#     return nth_fib(n-1)+nth_fib(n-2)

def nth_fib(n):
  a, b = 0, 1
  for i in range(n-1):
  	a, b = b, a + b
  return a
