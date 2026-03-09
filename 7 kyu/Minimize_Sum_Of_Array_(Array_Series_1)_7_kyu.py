# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python


# def min_sum(arr):
#     result = 0
#     arr = sorted(arr)
#     for i in range(0,len(arr)//2):
#         result += arr[i]*arr[-1-i]
#     return result


def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2)
