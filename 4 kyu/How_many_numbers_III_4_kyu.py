# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

# Solution_1
# def find_all(sum_dig, digs):
#     xs = [x for x in digis(digs) if sum(x) == sum_dig]
#     if not xs:
#         return []
#     else:
#         reduce_int = lambda xs: int(''.join(map(str,xs)))
#         min = reduce_int(xs[0])
#         max = reduce_int(xs[-1])
#         return [len(xs), min, max]

# def digis(digs,start=1):
#     """
#     >>> list(digs(3, start=9))
#     [[9, 9, 9]]
#     >>> list(digs(2, start=8))
#     [[8, 8], [8, 9], [9, 9]]
#     """
#     if digs == 1:
#         for x in range(start, 10):
#             yield[x]
#     else:
#         for x in range(start,10):
#             for y in digis(digs-1, x):
#                 yield[x]+y


# Solution_2
# from itertools import combinations_with_replacement

# def find_all(sum_dig, digs):
#     x = [int(''.join(x)) for x in combinations_with_replacement('123456789', digs) if sum(map(int, x)) == sum_dig]
#     return [len(x), min(x), max(x)] if len(x) > 0 else []



# Solution_3
from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]
