# Your task is to write an update for a lottery machine. Its current version produces a sequence of random letters and integers (passed as a string to the function). 
# Your code must filter out all letters and return unique integers as a string, in their order of first appearance. If there are no integers in the string return "One more run!"

# Examples
# "hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
# "ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
# "555"                   -->  "5"

# def lottery(s):
#     result = ""
#     for ch in s:
#         if ch.isdigit():
#             if ch not in result:
#                 result += ch
#     if result == "":
#         return 'One more run!'
#     return result

def lottery(s):
    return "".join(dict.fromkeys(filter(str.isdigit, s))) or "One more run!"
