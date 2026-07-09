# https://www.codewars.com/kata/56ba65c6a15703ac7e002075/train/python

# def find_next_power(val, pow_):
#     n = 1
#     while n ** pow_ <= val:
#         n += 1
#     return n ** pow_


def find_next_power(val, pow_):
    return int(val ** (1.0 / pow_) + 1) ** pow_
