# Return a string's even characters.
# Write a function that returns a sequence (index begins with 1) of all the even characters from a string.
# If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
# For example:
# "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
# "a"             --> "invalid string"

# def even_chars(st): 
#     if 2 > len(st) or len(st) > 100:
#         return "invalid string"
#     return list(st)[1::2]


def even_chars(st): 
    if 2 > len(st) or len(st) > 100:
        return "invalid string"
    return [list(st)[ch] for ch in range(1,len(list(st)),2)]
