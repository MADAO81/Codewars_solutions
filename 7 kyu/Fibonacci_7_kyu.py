# https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af/train/python

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     a,b = 0,1
#     for x in range(2,n+1):
#         a,b = b,a+b
#     return b

def fibonacci(n: int) -> int:
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x
