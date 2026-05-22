# https://www.codewars.com/kata/5375f921003bf62192000746/train/python

# import re
# def abbreviate(s):
#     words = re.split('([^a-zA-Z])',s)
#     result = []
#     return ''.join([i if not i.isalnum() or len(i) < 4 else i[0] + str(len(i)-2)+ i[-1] for i in words])


# def abbreviate(s):
#     mutate = lambda w: w[0] + str(len(w) - 2) + w[-1] if len(w) > 3 else w
#     result, word = '', ''
#     for char in s:
#         if char.isalpha():
#             word += char
#         else:
#             result += mutate(word) + char
#             word = ''
#     result += mutate(word)
#     return result


import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)
