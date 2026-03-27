# Write a function that removes every lone 9 that is inbetween 7s.

# "79712312" --> "7712312"
# "79797"    --> "777"


# import re

# def seven_ate9(str_):
#     while '797' in str_:
#         str_ = re.sub(r'797',r'77',str_)
#     return str_


def seven_ate9(str_):
    while "797" in str_:
        str_ = str_.replace("797", "77")
    return str_
