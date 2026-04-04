# Complete the function that returns an array of length n, 
# starting with the given number x and the squares of the previous number. 
# If n is negative or zero, return an empty array/list.

# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]

# def squares(x, n):
#     result = []
#     if n<=0:
#         return result
#     result = [x]
#     for i in range(n-1):
#         x = x**2
#         result.append(x)
#     return result

def squares(x,n):
    return [x**(2**i) for i in range(n)]
