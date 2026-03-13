# https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python

# import math

# def fold_array(array, runs):
#     for i in range(runs):
#         array = fold(array)
#     return array

# def fold(array):
#     if len(array) == 1:
#         return array
#     result = []
#     start = 0
#     end = len(array)-1
#     while start != end and start < end:
#         result.append(array[start]+array[end])
#         start += 1
#         end -= 1
#     if len(array) % 2:
#         result.append(array[math.floor(len(array)/2)])
#     return result



# def fold(arr):
#     length = len(arr)
#     mid = length // 2
#     return [a + b for a, b in zip(arr, arr[-1:-mid-1:-1])] + [arr[mid]] * (length & 1)
    
# def fold_array(array, runs):
#     ret = array
#     for __ in range(runs):
#         ret = fold(ret)
#     return ret



def fold_array(array, runs):
    mid = len(array) // 2
    a = [sum(pair) for pair in zip(array[:mid] + [0], reversed(array[mid:]))]
    return fold_array(a, runs - 1) if runs > 1 else a
