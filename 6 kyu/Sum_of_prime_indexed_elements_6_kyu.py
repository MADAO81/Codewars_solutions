# https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python

# def is_prime(n):
#     if n <2:
#         return False
#     for i in range(2,int(n*0.5)+1):
#         if n % i == 0:
#             return False
#     return True
    
    
# def total(arr):
#     return sum(value for i, value in enumerate(arr) if is_prime(i))


def is_prime(n):
    return n >= 2 and all(n%i for i in range(2, 1+int(n**.5)))
    
def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))
