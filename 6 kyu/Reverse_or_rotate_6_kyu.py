# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python


def func(s):
    result = sum(int(x)**3 for x in s)
    if result % 2 == 0:
        return s[::-1]
    else:
        return s[1:] + s[0]

def revrot(s, sz):
    if not sz:
        return ''
    return ''.join(func(''.join(x)) for x in zip(*[iter(list(s))]*sz))
