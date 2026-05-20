# Valid Phone Number
# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# Examples:

# "(123) 456-7890"  => true
# "(1111)555 2345"  => false
# "(098) 123 4567"  => false



# def validPhoneNumber(phoneNumber):
#     number = ''
#     template = '(xxx) xxx-xxxx'
#     for l in phoneNumber:
#         if l.isdigit():
#             number += 'x'
#         else:
#             number += l
    
#     return number == template
    


# import re

# nums = '1234567890'

# def validPhoneNumber(pn):
#     if len(pn) != len("(123) 456-7890"):
#         return False  
#     elif pn[0] != '(':
#         return False
#     elif pn[1] not in nums or pn[2] not in nums or pn[3] not in nums:
#         return False
#     elif pn[4] != ')':
#         return False
#     elif pn[5] != ' ':
#         return False
#     elif pn[6] not in nums or pn[7] not in nums or pn[8] not in nums:
#         return False
#     elif pn[9] != '-':
#         return False
#     elif pn[10] not in nums or pn[11] not in nums or pn[12] not in nums or pn[13] not in nums:
#         return False
#     else:



def validPhoneNumber(phoneNumber):
    import re
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))
    
