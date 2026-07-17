# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python

# import re
# from math import comb

# def expand(expr):
#     # Разбираем выражение вида (ax+b)^n
#     # Находим часть в скобках и степень
#     match = re.match(r'\(([^)]+)\)\^(\d+)', expr)
#     if not match:
#         return expr
    
#     inner, n_str = match.groups()
#     n = int(n_str)
    
#     # Если степень 0, возвращаем "1"
#     if n == 0:
#         return "1"
    
#     # Разбираем inner вида ax+b или ax-b
#     # Ищем переменную (одна буква)
#     var_match = re.search(r'[a-zA-Z]', inner)
#     if not var_match:
#         return expr
    
#     var = var_match.group()
    
#     # Разбиваем на части: коэффициент при x и свободный член
#     # Удаляем переменную из выражения
#     parts = inner.replace(var, '').split('+')
    
#     # Обрабатываем случай с минусом
#     if len(parts) == 1 and '-' in inner:
#         parts = inner.replace(var, '').split('-')
#         if inner.startswith('-'):
#             a = -1 if parts[0] == '' or parts[0] == '-' else -int(parts[0]) if parts[0] else -1
#         else:
#             a = int(parts[0]) if parts[0] else 1
#         b = -int(parts[1]) if len(parts) > 1 and parts[1] else 0
#     else:
#         # Стандартный случай
#         a = 0
#         b = 0
#         for part in parts:
#             if part == '' or part == '+':
#                 continue
#             if var in part or (part and part[-1] in '+-'):
#                 # Это коэффициент при x
#                 part_clean = part.replace(var, '')
#                 if part_clean == '' or part_clean == '+':
#                     a = 1
#                 elif part_clean == '-':
#                     a = -1
#                 else:
#                     a = int(part_clean)
#             else:
#                 b = int(part)
    
#     # Альтернативный способ разбора - более надежный
#     # Ищем a и b через регулярное выражение
#     # Формат: (ax+b)^n или (ax-b)^n
    
#     # Найдем коэффициент a
#     if inner.startswith('-'):
#         if var in inner[1:]:
#             a_part = inner[1:inner.index(var)]
#             a = -1 if a_part == '' else -int(a_part)
#         else:
#             # случай типа (-x-1)
#             pass
#     elif inner.startswith(var):
#         a = 1
#     else:
#         a_part = inner[:inner.index(var)]
#         a = int(a_part) if a_part else 1
    
#     # Найдем b
#     var_pos = inner.index(var)
#     rest = inner[var_pos+1:]
#     if rest:
#         if rest.startswith('+'):
#             b = int(rest[1:]) if rest[1:] else 0
#         elif rest.startswith('-'):
#             b = int(rest) if rest != '-' else -1
#         else:
#             b = int(rest)
#     else:
#         b = 0
    
#     # Если a == 0, то выражение просто b^n
#     if a == 0:
#         return str(b ** n)
    
#     # Генерируем члены разложения по формуле бинома Ньютона
#     terms = []
#     for k in range(n + 1):
#         coeff = comb(n, k) * (a ** (n - k)) * (b ** k)
#         if coeff == 0:
#             continue
        
#         power = n - k
        
#         # Формируем член
#         if power == 0:
#             term = str(coeff)
#         elif power == 1:
#             if coeff == 1:
#                 term = var
#             elif coeff == -1:
#                 term = '-' + var
#             else:
#                 term = str(coeff) + var
#         else:
#             if coeff == 1:
#                 term = var + '^' + str(power)
#             elif coeff == -1:
#                 term = '-' + var + '^' + str(power)
#             else:
#                 term = str(coeff) + var + '^' + str(power)
        
#         terms.append(term)
    
#     # Собираем результат
#     result = terms[0]
#     for term in terms[1:]:
#         if term.startswith('-'):
#             result += term
#         else:
#             result += '+' + term
    
#     return result


import re

P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

def expand(expr):
    a,v,b,e = P.findall(expr)[0]
    
    if e=='0': return '1'
    
    o   = [int(a!='-' and a or a and '-1' or '1'), int(b)]
    e,p = int(e), o[:]
    
    for _ in range(e-1):
        p.append(0)
        p = [o[0] * coef + p[i-1]*o[1] for i,coef in enumerate(p)]
    
    res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef in enumerate(p) if coef)
    
    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
