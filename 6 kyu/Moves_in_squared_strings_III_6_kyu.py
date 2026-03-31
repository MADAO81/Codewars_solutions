# https://www.codewars.com/kata/56dbeec613c2f63be4000be6/train/python

# def f(strng):
#     return [list(x) for x in strng.split('\n')], len(strng.split('\n'))
# def g(strng):
#     return '\n'.join([''.join(x) for x in strng])
# def rot_90_clock(strng):
#     strng,n = f(strng)
#     return g([strng[n-j-1][i] for j in range(n)] for i in range(n))
    

# def diag_1_sym(strng):
#     strng,n = f(strng)
#     return g([strng[j][i] for j in range(n)] for i in range(n))

# def selfie_and_diag1(strng):
#     a,n = f(strng)
#     b,n = f(diag_1_sym(strng))
#     return '\n'.join([''.join(x)+'|'+''.join(y) for x,y in zip(a,b)])

# def oper(fct, s):
#     return fct(s)


def rot_90_clock(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n')[::-1]))      
def diag_1_sym(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n'))) 
def selfie_and_diag1(strng):
    return '\n'.join('|'.join(x) for x in zip(strng.split('\n'), diag_1_sym(strng).split('\n')))
def oper(fct, s):
    return fct(s)
