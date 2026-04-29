# https://www.codewars.com/kata/58c9322bedb4235468000019/train/python

# def is_very_even_number(n):
#     if n == 0:
#         return True
#     else:
#         return (n-1)%9%2 != 0


# def is_very_even_number(n):
#     return n == 0 or (n - 1) % 9 % 2



def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return True if n % 2 == 0 else False
