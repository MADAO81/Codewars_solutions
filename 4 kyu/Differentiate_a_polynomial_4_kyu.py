# https://www.codewars.com/kata/566584e3309db1b17d000027/train/python

# import re

# def differentiate(equation, point):
#     terms = re.findall(r'([+-]?\d*)(x(?:\^\d+)?)?', equation.replace(' ', ''))
#     derivative = 0
    
#     for term in terms:
#         coef, variable = term
        
#         if variable:
#             if '^' in variable:
#                 exp = int(variable.split('^')[1])
#             else:
#                 exp = 1
                
#             if coef == '' or coef == '+':
#                 coef = 1
#             elif coef == '-':
#                 coef = -1
#             else:
#                 coef = int(coef)
            
#             if exp == 1:
#                 derivative += coef
#             else:
#                 derivative += coef * exp * point ** (exp-1)
#         else:
#             continue
            
#     return derivative


from collections import defaultdict
import re

P = re.compile(r'\+?(-?\d*)(x\^?)?(\d*)')

def differentiate(eq, x):
    
    derivate = defaultdict(int)
    for coef,var,exp in P.findall(eq):
        exp  = int(exp or var and '1' or '0')
        coef = int(coef!='-' and coef or coef and '-1' or '1')
        
        if exp: derivate[exp-1] += exp * coef
    
    return sum(coef * x**exp for exp,coef in derivate.items())
