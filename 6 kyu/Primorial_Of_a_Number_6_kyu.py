# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python


# import numpy as np

# def is_prime(num):
#     remains = num % np.arange(1, num+1)
#     return len(remains[remains == 0]) == 2

# def num_primorial(n):
#     total = 1
#     prime_number_count = 0
#     number = 2
#     while prime_number_count < n:
#         if is_prime(number) == True:
#             total *= number
#             prime_number_count += 1
#         number += 1
        
#     return total


def num_primorial(n):
    primorial, x, n = 2, 3, n-1
    while n:
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primorial *= x
            n -= 1
        x += 2
    return primorial
