# https://www.codewars.com/kata/5413759479ba273f8100003d/train/python

# def reverse(lst):
#     out = list()
#     for i in range(len(lst)-1,-1,-1):
#         out.append(lst[i])
#     return out


# def reverse(lst):
#     empty_list = list()            # use this!
#     result = list()
#     while lst:
#         result.append(lst.pop())
#     return result


# from collections import deque

# def reverse(lst):
#     q = deque()
#     for x in lst:
#         q.appendleft(x)
#     return list(q)


# def reverse(lst):
#     out = list()
#     for x in lst:
#         out.insert(0, x)
#     return out

def reverse(lst):
    empty_list = list()
    for i in range(len(lst)):
        empty_list.append(lst.pop())
    return empty_list
