# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b/train/python

# from math import prod as product
# from statistics import mean, median

# def enum(n, m=1):
#     yield [n]
#     for i in range(m, n//2+1):
#         for j in enum(n-i, i):
#             yield [i] + j

# def prod(n):
#     return set(sorted([product(p) for p in enum(n)]))

# def part(n):
#     p = list(prod(n))
#     return 'Range: {} Average: {:.2f} Median: {:.2f}'.format(max(p)-min(p), mean(p), median(p))



def prod(n):
    ret = [{1.}]
    for i in range(1, n+1):
        ret.append({(i - x) * j for x, s in enumerate(ret) for j in s})
    return ret[-1]

def part(n):
    p = sorted(prod(n))
    return "Range: %d Average: %.2f Median: %.2f" % \
            (p[-1] - p[0], sum(p) / len(p), (p[len(p)//2] + p[~len(p)//2]) / 2)
