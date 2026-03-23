# Strip Comments
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas



# def strip_comments(strng, markers):
#     s_list = strng.split('\n')
#     for marker in markers:
#         s_list = [item.split(marker)[0].rstrip() for item in s_list]
#     return '\n'.join(s_list)



import re
def solution(string, markers):
    return string if not markers else re.sub(f" *[{re.escape(''.join(markers))}].*", "", string, re.MULTILINE)
