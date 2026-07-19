# https://www.codewars.com/kata/5245a9138ca049e9a10007b8/train/python

from itertools import groupby

def count_adjacent_pairs(st): 
    return sum(1 for x, group in groupby(st.lower().split()) if len(list(group))>1)
