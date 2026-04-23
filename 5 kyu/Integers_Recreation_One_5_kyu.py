# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

# import math
# def list_squared(m, n):
#     square = lambda n: int(math.sqrt(n) + 0.5) ** 2 == n
#     result = []
#     for i in range(m, n):
#         s = sum([j**2 for j in range(1, i+1) if i%j==0])
#         if square(s): result.append([i, s])
#     return result

# import math
# def list_squared(m, n):
#     result = []
#     for number in range(m, n+1):
#         sum_of_squared = 0
#         for i in range(1, int(math.sqrt(number)+1)):
#             if number % i == 0:
#                 sum_of_squared += i * i
#                 if number // i != i:
#                     sum_of_squared += (number // i) * (number // i)
#         root = math.sqrt(sum_of_squared)
#         if root == int(root):
#             result.append([number, sum_of_squared])
#     return result


def list_squared(m, n):
    out = []
    for i in range(m,n+1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range (1,int(i**0.5)+1) if i%x == 0])
        # And adding their counterpart
        possibles.update([i/x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x**2 for x in possibles)
        # Checking for exact square
        if (int(val**0.5))**2 == val: out.append([i, val])
    return out
