# https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python

def middle_permutation(string):
    s = sorted(string)
    if len(s) % 2 == 0:
        return s.pop(len(s)//2 - 1) + ''.join(s[::-1])
    else:
        return s.pop(len(s)//2) + middle_permutation(''.join(s))
