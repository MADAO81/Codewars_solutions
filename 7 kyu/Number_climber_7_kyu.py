# https://www.codewars.com/kata/559760bae64c31556c00006b/train/python

# def climb(n):
#     result = []
#     while n>1:
#         result.insert(0,n)
#         n = n//2
#     result.insert(0,n)
#     return result



# def climb(n):
#     return [n >> i for i in range(len(f"{n:b}") - 1, -1, -1)]




def climb(n):
    sequence = []
    while n > 0:
        sequence.append(n)
        n //= 2
    return sequence[::-1]
