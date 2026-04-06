# https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/train/python

# def stanton_measure(arr):
#     num_one = 0
#     num_des = 0
#     for i in arr:
#         if i == 1:
#             num_one += 1
#     for j in arr:
#         if j == num_one:
#             num_des += 1
#     return num_des

def stanton_measure(arr):
    return arr.count( arr.count(1) )
