# Simple Fun #198: Cake Slice
# Task
# A cake is sliced with n straight lines. Your task is to calculate the maximum number of pieces the cake can have.

# Example
# For n = 0, the output should be 1.

# For n = 1, the output should be 2.

# For n = 2, the output should be 4.

# For n = 3, the output should be 7.


# def cake_slice(n):
#     return (n ** 2 + n + 2) // 2

# def cake_slice(n):    
#     x = 1
#     for i in range(0,n+1):
#         x += i
#     return x



def cake_slice(n):
    count = 0
    slices = 1
    while count != n:
        count +=1
        slices += count
    return slices
