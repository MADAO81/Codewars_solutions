# https://www.codewars.com/kata/5d59576768ba810001f1f8d6/train/python

# def quadratic(x1, x2):
#     return (1,-x1-x2,x1*x2)

def quadratic(x1, x2):
    b = -(x1+x2)
    c = x1*x2
    return (1,b,c)
