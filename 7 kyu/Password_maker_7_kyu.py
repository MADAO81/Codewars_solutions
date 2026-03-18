# https://www.codewars.com/kata/5637b03c6be7e01d99000046/train/python

# def make_password(phrase):
#     result = ''
#     substitute = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5',}
#     for i in phrase.split():
#         result += i[0]
#     for key,value in substitute.items():
#         result = result.replace(key,value)
#     return result



# import re
# def make_password(phrase):
#     letters =''.join(re.findall(r'\b\w',phrase))
#     table = str.maketrans({
#         'o': '0', 'O': '0',
#         'i': '1', 'I': '1',
#         's': '5', 'S': '5'
#     })
#     return letters.translate(table)


SWAP = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}

def make_password(phrase):
    return ''.join(SWAP.get(a[0], a[0]) for a in phrase.split())
