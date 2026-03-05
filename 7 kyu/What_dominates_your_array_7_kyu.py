# https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python


# from collections import Counter

# def dominator(arr):
#     if not arr:
#         return -1
#     k, v = Counter(arr).most_common(1)[0]
#     return k if v > len(arr) / 2 else -1
  

def dominator(arr):
    for el in arr:
        if arr.count(el)>len(arr)//2:
            return el
    return -1
