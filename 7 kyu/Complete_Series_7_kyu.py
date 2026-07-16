# https://www.codewars.com/kata/580a4001d6df740d61000301/train/python


def complete_series(seq): 
    return [0] if len(seq) != len(set(seq)) else list(range(max(seq) + 1))
