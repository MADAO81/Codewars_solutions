# https://www.codewars.com/kata/592edfda5be407b9640000b2/train/python

# def decode(code, key):
#     key_str= str(key)
#     return ''.join(chr(code[i] - int(key_str[i % len(key_str)]) + ord('a') - 1) for i in range(len(code)))


from itertools import cycle
from string import ascii_lowercase

def decode(code, key):
    keys = cycle(map(int, str(key)))
    return ''.join(ascii_lowercase[n - next(keys) - 1] for n in code)
