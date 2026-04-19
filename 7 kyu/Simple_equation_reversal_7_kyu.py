# Given a mathematical equation that has *,+,-,/, reverse it as follows:

# solve("100*b/y") = "y/b*100"
# solve("a+b-c/d*30") = "30*d/c-b+a"




# import re

# def solve(eq):
#     return "".join(re.split("([*+-/])", eq)[::-1])


import re

def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))
