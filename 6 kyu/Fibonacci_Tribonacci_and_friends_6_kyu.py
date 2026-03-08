https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python

# def xbonacci(signature, n):
#     result = signature[:]
    
#     for i in range(n-len(signature)):
#         current_fib = 0
#         start = len(result) - len(signature)
#         for j in result[start:]:
#             current_fib += j
#         result.append(current_fib)
#     return result[:n]


def xbonacci(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output
