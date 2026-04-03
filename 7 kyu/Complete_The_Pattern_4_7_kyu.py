# https://www.codewars.com/kata/55736129f78b30311300010f/train/python


# def pattern(n):
#     result = []
#     for i in range(n+1):
#         lst = list(range(i+1, n+1))
#         result.append(''.join(str(x) for x in lst))
#     return '\n'.join(result)[:-1]



def pattern(n):
    return '\n'.join( ''.join(str(j) for j in range(i,n+1)) for i in range(1,n+1) )
