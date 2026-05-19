# https://www.codewars.com/kata/550527b108b86f700000073f/train/python

# from math import pi

# def iter_pi(epsilon):
#     count = 1
#     my_pi =  4.0
#     while abs(pi - my_pi) > epsilon:
#         if count % 2:
#             my_pi -= (1.0 /(count * 2 + 1)) * 4
#         else:
#             my_pi += (1.0 / (count * 2 + 1)) * 4
#         count += 1
#     return [count, round(my_pi, 10)]




# import math


# def iter_pi(epsilon):
#     """
#     Calculates decimals of PI using Leibniz formula.

#     Parameters
#     ----------
#     epsilon : float
#         Precision value for calculation.

#     Returns
#     -------
#     list
#         Result in form: precision, PI approximation.
#     """

#     n = 1
#     estim = 4
#     while abs(estim - math.pi) > epsilon:
#         n += 1
#         estim += (-4, 4)[n % 2] / (2 * n - 1.0)
    
#     res = [n, round(estim, 10)]
#     return res




from math import pi

def iter_pi(epsilon):
    n = 1
    approx = 4
    while abs(approx - pi) > epsilon:
        n += 1
        approx += (-4, 4)[n % 2] / (n * 2 - 1.0)
    return [n, round(approx, 10)]
