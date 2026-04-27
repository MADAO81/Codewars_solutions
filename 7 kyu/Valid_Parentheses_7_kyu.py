# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100

# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.

# Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!



# def valid_parentheses(paren_str):
#     flag = 0
#     for parenth in paren_str:
#         if parenth == "(":
#             flag +=1
#         elif parenth == ")":
#             flag -=1
#         if flag < 0:
#             return False
#     return True if flag == 0 else False



def valid_parentheses(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""
