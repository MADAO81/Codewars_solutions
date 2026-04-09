# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

# def parse_int(string):
#     digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
#               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
#               'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
#               'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
#               'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
#               'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
#               'eighty': 80, 'ninety': 90} 
#     breakpoints = {'hundred': '00', 'thousand': '000', 'million': '000000'}
#     string = string.replace("-", " ").split(" ")
#     if len(string) == 1: return digits[string[0]]
#     result = []
#     temp_sum = 0
#     counter = 0
#     length = 1
#     if 'hundred' in string: 
#         length = 3
#     if 'thousand' in string: 
#         length = 4
#     if 'million' in string: 
#         length = 7
#     while counter < len(string):
#         s = string[counter]
#         if s != "" and s != 'and':
#             if s in digits: 
#                 temp_sum += digits[s]
#             if s in breakpoints:
#                 temp_sum = int(str(temp_sum) + breakpoints[s])
#             if len(str(temp_sum)) >= length:
#                 result.append(temp_sum)
#                 if length == 7: 
#                     length = 4
#                 elif length == 4: 
#                     length = 3
#                 else: 
#                     length = 1
#                 temp_sum = 0
#         counter += 1
#     return sum(result + [temp_sum])


# words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
# words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
# thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
# def parse_int(strng):
#     num = group = 0
#     for w in strng.replace(' and ', ' ').replace('-', ' ').split():
#         if w == 'hundred': group *= words[w]
#         elif w in words: group += words[w]
#         else:
#             num += group * thousands[w]
#             group = 0
#     return num + group



ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)
