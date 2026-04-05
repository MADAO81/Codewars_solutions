# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

# def gap(g, m, n):
#     start = 0
#     end = 0
#     for i in range(m,n+1):
#         if is_prime(i):
#             print (i)
#             if start == 0:
#                 start = i
#             elif end == 0:
#                 end = i
#             else:
#                 start = end
#                 end = i 
#         if end - start == g:
#             return [start, end]
#     return None

# def is_prime(n):
#     if n<=0 or n == 1:
#         return False
#     i = 2
#     while (i<=n**0.5):
#         if n % i == 0:
#             return False
#         i +=1
#     return True


def gap(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g: 
                return [previous_prime, i]
            previous_prime = i
    return None
            
    
def is_prime(n):
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True
