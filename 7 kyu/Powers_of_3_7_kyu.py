# Powers of 3
# Given a positive integer N, return the largest integer k such that 3^k < N.

# For example,

# 3 --> 0
# 4 --> 1
# You may assume that the input to your function is always a positive integer.

def largest_power(N):
    k = 0
    while pow(3,k) < N:
        k +=1
    return k-1
