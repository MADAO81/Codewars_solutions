# https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/python

# from collections import deque

# def rotate(str_):
#     dq = deque(str_)
#     result = []
#     for i in range(len(str_)):
#         dq.rotate(-1)
#         result.append(''.join(dq))
#     return result 


# def rotate(str):
#     l = []
#     for i in str:
#         str = str[1:] + str[0]
#         l.append(str)
#     return l


def rotate(str_):
    return [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]
