# https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

# def tidyNumber(n):
#     return n== int("".join(sorted(str(n))))

def tidyNumber(n):
    s = list(str(n))
    return s == sorted(s)
