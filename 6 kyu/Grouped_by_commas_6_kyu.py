# https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python


# def group_by_commas(n):
#     n = str(n)[::-1]
#     return ",".join([n[i:i + 3] for i in range(0, len(n), 3)])[::-1]


def group_by_commas(n):
    return '{:,}'.format(n)
