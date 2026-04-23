# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python

"""
0 < x < y <= n
sum = (n(n + 1)) / 2
sum - (x + y) = xy
sum = xy + x + y = (x + 1)(y + 1) - 1
sum + 1 = (x + 1)(y + 1)
"""


# def removNb(n):
#     target = 1 + ((n * (n + 1)) / 2)
#     pairs = []
#     for x in xrange(target / (n + 1), n + 2):
#         if target % x != 0:
#             continue
#         pairs.append((x - 1, (target / x) - 1))
#     return pairs

def remov_nb(n):
    equal = []
    sum = n * (1+n) / 2 
    for i in range(1,n+1):
        j = (sum-i)/(i+1)
        if j == int(j) and j <= n+1 and i !=j:
            equal.append((int(i), int(j)))
    return equal
