# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/train/python



# def height(n, m):
#     h, t = 0, 1
#     for i in range(1, n + 1): 
#         t = t * (m - i + 1) // i
#         h += t
#     return h



def height(n, m):
    if n == 0 or m == 0:
        return 0
    
    # If we have more eggs than attempts, we can only use m eggs effectively
    n = min(n, m)
    
    total = 0
    # Calculate combinations iteratively
    # C(m, 1) = m
    # C(m, k) = C(m, k-1) * (m - k + 1) // k
    
    # Start with C(m, 0) = 1, but we need C(m, 1)
    c = m  # C(m, 1)
    total += c
    
    for k in range(2, n + 1):
        c = c * (m - k + 1) // k
        total += c
    
    return total
    return dp[n]
