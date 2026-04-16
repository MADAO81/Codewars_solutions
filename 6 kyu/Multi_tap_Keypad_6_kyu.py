# Multi-tap Keypad Text Entry on an Old Mobile Phone
# https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python


# def presses(phrase):
#     result = 0
#     for x in phrase.upper():
#         for t in ['1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0', '*', '#']:
#             if x in t:
#                 result += t.index(x) + 1
#     return result


BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)
