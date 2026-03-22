# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python

# from itertools import groupby

# def remove_consecutive_duplicates(s):
#     return ' '.join(k for k,_ in groupby(s.split()))

import re
def remove_consecutive_duplicates(s):
    return re.sub(r"\b(\w+)(\s(\1\b))+", r"\1", s)
