# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


# Solution_1
# def snail(snail_map):
#     results = []
#     while len(snail_map) > 0:
#         # right
#         results += snail_map[0] 
#         del snail_map[0]
        
#         if len(snail_map) > 0:
#             # down
#             for i in snail_map:
#                 results += [i[-1]]
#                 del i[-1]
                
#             # left
#             if snail_map[-1]:
#                 results +=snail_map[-1][::-1]
#                 del snail_map[-1]
                
#             # top
#             for i in reversed(snail_map):
#                 results +=[i[0]]
#                 del i[0]
                
#     return results



# Solution_2

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m
