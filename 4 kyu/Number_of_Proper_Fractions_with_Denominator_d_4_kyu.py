# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python


def proper_fractions(n):
    if n <= 1:
        return 0
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p == 2 else 2
        
    if n > 1:
        result -= result // n
    return result

