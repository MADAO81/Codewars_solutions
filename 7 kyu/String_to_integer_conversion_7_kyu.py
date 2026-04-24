# https://www.codewars.com/kata/54fdadc8762e2e51e400032c/train/python

# def my_parse_int(strn):
#     if strn.strip().isdigit():
#         return int(strn)
#     return 'NaN'


# def my_parse_int(s):
#     return int(s) if s.strip().isdigit() else "NaN"


def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'
