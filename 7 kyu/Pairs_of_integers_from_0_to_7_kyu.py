# https://www.codewars.com/kata/588e27b7d1140d31cb000060/solutions/python

# def generate_pairs(n):
#     result = []
#     for a in range(n+1):
#         for b in range(a,n+1):
#             result.append([a,b])
#     return result

def generate_pairs(n):
    return [[i,j] for i in range(n+1) for j in range(i, n+1)]
