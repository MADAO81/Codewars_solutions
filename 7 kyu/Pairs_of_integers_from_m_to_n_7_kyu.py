# https://www.codewars.com/kata/588e2a1ad1140d31cb00008c/train/python


# def generate_pairs(m, n):
#     a=[]
#     for x in range(m,n+1):
#         for y in range(m,n+1):
#             if y>=x:
#                 a.append((x,y))
#     return a   



def generate_pairs(m, n):
    return [(a,b) for a in range(m,n+1) for b in range(a,n+1)]
