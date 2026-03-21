# https://www.codewars.com/kata/5784c89be5553370e000061b/train/python

def max_product(a):
    x = max(a)
    a.remove(x)
    y = max(a)
    return x*y
