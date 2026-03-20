# https://www.codewars.com/kata/586538146b56991861000293/train/python

from preloaded import NATO # NATO['A'] == 'Alfa', etc

# def to_nato(words : str) -> str:
#     telephony = {
#         'a':'Alfa',
#         'b':'Bravo',
#         'c':'Charlie',
#         'd':'Delta',
#         'e':'Echo',
#         'f':'Foxtrot',
#         'g':'Golf',
#         'h':'Hotel',
#         'i':'India',
#         'j':'Juliett',
#         'k':'Kilo',
#         'l':'Lima',
#         'm':'Mike',
#         'n':'November',
#         'o':'Oscar',
#         'p':'Papa',
#         'q':'Quebec',
#         'r':'Romeo',
#         's':'Sierra',
#         't':'Tango',
#         'u':'Uniform',
#         'v':'Victor',
#         'w':'Whiskey',
#         'x':'Xray',
#         'y':'Yankee',
#         'z':'Zulu'}
    
#     result = ''
#     for ch in words.lower():
#         if ch == ' ':
#             continue
#         result += ' '
#         if ch in telephony:
#             result += telephony[ch]
#         else:
#             result += ch
#     return result.strip()


def to_nato(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
