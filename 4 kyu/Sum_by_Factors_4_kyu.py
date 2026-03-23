# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

# def sum_for_list(lst):
#     mp = {}
#     for i in lst:
#         for j in factors(abs(i)):
#             if not mp.get(j):
#                 mp.setdefault(j,i)
#                 continue
#             mp[j] += i
#     return sorted(list(element) for element in mp.items())

# def factors(n):
#     factors_numbers = []
#     prime = 2
#     while prime * prime <= n:
#         while n%prime == 0:
#             factors_numbers.append(prime)
#             n //=prime
#         prime += 1
#     if n>1:
#         factors_numbers.append(n)
#     return set(factors_numbers)

from collections import defaultdict
def sum_for_list(lst):

    def factors(x):
        p_facs = []
        i = 2
        while x > 1 or x < -1:
            if x % i == 0:
                p_facs.append(i)
                x //= i
            else:
                i += 1
        return list(set(p_facs))
    
    fac_dict = defaultdict(int)
    
    for i in lst:
        for fac in factors(i):
            fac_dict[fac] += i
            
    return sorted([[k,v] for k,v in fac_dict.items()])
