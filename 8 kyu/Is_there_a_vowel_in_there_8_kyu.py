# Is there a vowel in there?
# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.

# def is_vow(inp):
#     result = []
#     acsii_values = [101, 105, 111, 117, 97,]
#     for i in inp:
#         if i in acsii_values:
#             ascii_symbol = str(chr(i))
#             result.append(ascii_symbol)
#         else:
#             result.append(i)
#     return result
    
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]
