# Simple Fun #176: Reverse Letter
# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
# Example
# For str = "krishan", the output should be "nahsirk".
# For str = "ultr53o?n", the output should be "nortlu".
# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.
# [output] a string


# def reverse_letter(st):
#     return "".join([x for x in st[::-1] if x.isalpha()])


import re
def reverse_letter(st):
    return re.sub("[^a-zA-Z]","",st)[::-1]
