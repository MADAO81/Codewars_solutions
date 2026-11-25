# Sum The Strings
# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

# Example: (Input1, Input2 -->Output)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

# def sum_str(a, b):
#     user_list = []
#     if a == "":
#         a = 0
#         user_list.append(a)
#     else:
#         user_list.append(int(a))
#     if b == "":
#         b = 0
#         user_list.append(b)
#     else:
#         user_list.append(int(b))
#     total = sum(user_list)
#     return str(total)
    
    
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
