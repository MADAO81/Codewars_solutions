# https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

# from collections import Counter
# def paint_letterboxes(start, finish):
#     return [Counter("".join(map(str,range(start,finish+1))))[str(x)] for x in range(10)]


# from collections import Counter
# def paint_letterboxes(s, f):
#     a = Counter("".join(map(str, range(s, f+1))))
#     return [a[x] for x in "0123456789"]
  

# def paint_letterboxes(start, finish):
#     xs = [0] * 10
#     for n in range(start, finish+1):
#         for i in str(n):
#             xs[int(i)] += 1
#     return xs


def paint_letterboxes(start, finish):
    boxes = ''.join([str(b) for b in range(start,finish+1)])
    return [boxes.count(n) for n in '0123456789']
