# Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

# 0 => [ ]
# 1 => [ [1] ]
# 2 => [ [1], [1, 1] ]
# 3 => [ [1], [1, 1], [1, 1, 1] ]



# def pyramid(n):
#     return [[1 for x in range(i)] for i in range(1, n+1)]


def pyramid(n):
    return [[1]*x for x in range(1, n+1)]
