# https://www.codewars.com/kata/57073869924f34185100036d/train/python


# import random
# def random_case(x):
#     return ''.join(ch.upper() if random.choice([True, False]) else ch.lower() for ch in x)
    


import random

def random_case(x):
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])
