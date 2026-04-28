# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python

# def name_value(my_list):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     output = []
#     for i, chars in enumerate(my_list):
#         total = 0
#         for char in chars:
#             if char in letters:
#                 total += letters.index(char) + 1
#         output.append(total*(i+1))
#     return output

def nameValue(myList):
    return [ i*sum(map(lambda c: [0, ord(c)-96][c.isalpha()], w.lower())) for i,w in enumerate(myList,1)]
