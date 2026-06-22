# https://www.codewars.com/kata/5bd00c99dbc73908bb00057a/train/python


# def alpha_seq(string):
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     output = ''
#     for s in ''.join(sorted((string.lower()))):
#         output += s.upper()
#         output += s * alpha.find(s)
#         output += ','
#     return output.strip(',')



def alpha_seq(strng):
    return ','.join(char.upper()+char*(ord(char)-96-1) for char in sorted(strng.lower()))
