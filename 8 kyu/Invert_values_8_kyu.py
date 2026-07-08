# Invert values
# Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.
# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []

def invert(lst):
        return [i*-(1) for i in lst]
