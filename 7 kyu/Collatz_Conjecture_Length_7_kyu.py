# https://www.codewars.com/kata/54fb963d3fe32351f2000102/train/python

# def collatz(n):
#     return 1 if n == 1 else 1 + collatz(3 * n + 1 if n % 2 else n // 2)

def collatz(n):
    steps = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
