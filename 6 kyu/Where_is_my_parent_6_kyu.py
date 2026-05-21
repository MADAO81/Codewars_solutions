# https://www.codewars.com/kata/58539230879867a8cd00011c/train/python

# def find_children(dancing_brigade):
#     lowered = dancing_brigade.lower()
#     unique = sorted(set(lowered))
#     result = ''
#     for el in unique:
#         counted_el = dancing_brigade.count(el)
#         result += el.upper() + el * counted_el
#     return result


def find_children(s):
    return ''.join( sorted(sorted(s), key=str.lower) )
