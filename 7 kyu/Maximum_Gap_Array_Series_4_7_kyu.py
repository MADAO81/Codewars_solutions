# https://www.codewars.com/kata/5a7893ef0025e9eb50000013/train/python

# import numpy as np
# def max_gap(numbers):
#     numbers = np.array(sorted(numbers))
#     return np.max(numbers[1:]-numbers[:-1])


# import numpy
# def max_gap(numbers):
#     return max(numpy.diff(sorted(numbers)))


def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:]))
