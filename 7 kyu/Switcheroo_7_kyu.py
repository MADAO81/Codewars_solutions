# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

# Example:

# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

# def switcheroo(s):
#     result = ""
#     for ch in s:
#         if ch == "a":
#             result +="b"
#         elif ch == "b":
#             result +="a"
#         elif ch == "c":
#             result += "c"
#     return result

def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))
