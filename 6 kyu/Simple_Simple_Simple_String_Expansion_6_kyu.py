# https://www.codewars.com/kata/5ae326342f8cbc72220000d2/train/python



# def string_expansion(s):
#     result =""
#     n=1
#     for i in range(len(s)):
#         if  s[i]>="0" and s[i]<="9":
#             n=int(s[i])
#         else:
#             for j in range(n):
#                 result += s[i] 
#     return result



# import re

# def string_expansion(s):
#     return ''.join(''.join(int(n or '1')*c for c in cc) for n,cc in re.findall(r'(\d?)(\D+)', s))


def string_expansion(s):
    m,n = '',1
    for j in s:
        if j.isdigit():
            n = int(j)
        else:
            m += j*n
    return m
