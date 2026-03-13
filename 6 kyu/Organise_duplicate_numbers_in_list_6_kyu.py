# https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python


# def group(arr):
#     if not arr:
#         return arr
#     result = []
#     temp = []
#     duplicate = []
#     for num in arr:
#         if num in duplicate:
#             continue
#         count = arr.count(num)
#         duplicate.append(num)
#         while count !=0:
#             temp.append(num)
#             count -= 1
#         result.append(temp)
#         temp = []
        
#     return result



# from collections import Counter

# def group(arr):
#     return [[k] * n for k, n in Counter(arr).items()]




group=lambda arr: [[n]*arr.count(n) for n in sorted(set(arr), key=arr.index)]
