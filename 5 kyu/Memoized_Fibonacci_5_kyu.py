# https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python


# def fibonacci(n, memorize={}):
#     if n in memorize:
#         return memorize[n]
#     elif n <= 2:
#         return 1
#     else:
#         memorize[n] = fibonacci(n-1, memorize) + fibonacci(n-2, memorize)
#         return memorize[n]


# def memoized(f):
#     cache = {}
#     def wrapped(k):
#         v = cache.get(k)
#         if v is None:
#             v = cache[k] = f(k)
#         return v
#     return wrapped

# @memoized
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
  fib = [0,1]
  for i in xrange(2,n+1):
    fib.append(fib[i-1] + fib[i-2])
  return fib[n]

