# https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python

# import math

# def mixed_fraction(s):
#     x,y = [int(number) for number in s.split('/')]
#     if y == 0:
#         raise ZeroDivisionError
#     if x == 0:
#         return '0'
#     sign = '' if x*y > 0 else '-'
#     x,y = abs(x), abs(y)
#     a = x//y
#     b = x%y
#     c = y
#     gcd = math.gcd(b,c)
#     b = b//gcd
#     c = c//gcd
#     if a == 0:
#         return f"{sign}{b}/{c}" if sign else f"{b}/{c}"
#     else:
#         if b == 0:
#             return f"{sign}{a}"
#         else:
#             return f"{sign}{a} {b}/{c}"




# from fractions import Fraction

# def mixed_fraction(s):
#     f = Fraction(*map(int, s.split('/')))
#     if f.numerator == 0 or f.denominator == 1: return str(f)
#     (a, b), c = divmod(abs(f.numerator), f.denominator), f.denominator
#     return '-' * (f < 0) + f'{a} ' * bool(a) + f'{b}/{c}'




def gcd(a,b): return b if not a else gcd(b%a,a)

def sign(a): return a if a==0 else abs(a)/a

def mixed_fraction(s):
    a,b=[int(x) for x in s.split("/")]
    
    if int(b)==0: 
        raise ZeroDivisionError
        
    d,m=divmod(abs(a),abs(b))
    g = gcd(m,b)
    
    s = "-" if sign(a)*sign(b)==-1 else ""
    a = str(d) if d != 0 else ""
    b = "%i/%i" % (m/g,abs(b)/g) if m != 0 else ""
    
    return  s + " ".join([a,b]).strip() or "0"
