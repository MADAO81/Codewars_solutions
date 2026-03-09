# https://www.codewars.com/kata/57f7796697d62fc93d0001b8/train/python

# def trouble(x, t):
#     count = 0
#     while count < len(x)-1:
#         if x[count] + x[count+1] == t:
#             del x[count+1]
#         else: count += 1
#     return x


# def trouble(x, t):
#     res = []
#     for i in x:
#         if not res or res[-1] + i != t:
#             res.append(i)
#     return res


def trouble(x, t):
    arr = [x[0]]
    for c in x[1:]:
        if c + arr[-1] != t:
            arr.append(c)
    return arr
