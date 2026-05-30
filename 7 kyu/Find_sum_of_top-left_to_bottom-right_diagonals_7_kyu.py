# https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/python

# def diagonal_sum(array):
#     return sum(array[i][i] for i in range(len(array)))

def diagonal_sum(array):
    return sum(row[i] for i, row in enumerate(array))
