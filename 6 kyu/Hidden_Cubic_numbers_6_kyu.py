# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python

# import re
# def check_cubic(match):
#     match_int = int(match)
#     match = sum(list(map(lambda x: int(x)**3, list(match))))
#     return (match == match_int, match_int) 

# def is_sum_of_cubes(s):
#     matches = re.findall('[0-9]{1,3}', s)
#     output , total = '', 0
#     for match in matches:
#         res, num = check_cubic(match)
#         if res:
#             output += match + ' '
#             total += num
#     if output:
#         return output + str(total) + ' Lucky'
#     return 'Unlucky'


import re

PATTERN = re.compile(r'(\d{1,3})')

def is_sum_of_cubes(s):
    found = list(filter(lambda nStr: int(nStr) == sum(int(d)**3 for d in nStr), PATTERN.findall(s)))
    return "Unlucky" if not found else "{} {} {}".format(' '.join(found), sum(map(int, found)), 'Lucky')
