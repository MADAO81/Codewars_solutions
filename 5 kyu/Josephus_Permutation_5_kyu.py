# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python

# def josephus(items,k):
#     result = []
#     index = -1 
#     while items:
#         index = index + k
#         if index >= len(items):
#             index = index % len(items)
#         result.append(items.pop(index))
#         index -= 1
#     return result


from collections import deque

def josephus(items,k):
    q = deque(items)
    return [[q.rotate(1-k), q.popleft()][1] for _ in items]
