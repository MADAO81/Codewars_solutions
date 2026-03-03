# https://www.codewars.com/kata/529b418d533b76924600085d/train/python


# import re

# def to_underscore(strng: str) -> str:
#     return '_'.join(re.findall(r'[A-Z][a-z0-9]*',strng)).lower() if type(strng) is str else str(strng)


# def to_underscore(string):
#     string = str(string)
#     camel_case = string[0].lower()
#     for c in string[1:]:
#         camel_case += '_{}'.format(c.lower()) if c.isupper() else c
#     return camel_case


import re

def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()  
