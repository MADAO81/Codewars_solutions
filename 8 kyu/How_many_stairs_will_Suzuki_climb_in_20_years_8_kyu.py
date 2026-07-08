# https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e/train/python

def stairs_in_20(stairs):
    return sum(sum(day) for day in stairs)*20
