# https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python


# from scipy.special import comb
# def pascals_triangle(n):
#     return [comb(a, b, exact=True) for a in range(n) for b in range(a + 1)]   


def pascals_triangle(n):
    if n == 1:
        return [1]
    previous = pascals_triangle(n-1)
    return previous + [1 if i == 0 or i == n-1 else previous[-i] + previous[-(i+1)] for i in range(n)]
