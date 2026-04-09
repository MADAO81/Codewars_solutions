# https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python

# import re
# def simplify(poly: str) -> str:
#     polyDict = dict()
#     digitSortDict = dict()
#     alphaSortDict = dict()
#     lst = list()
#     regex = re.compile(r'''([+-])?(\d+)?([a-z]+) ''', re.VERBOSE)
#     mo = regex.findall(poly)
#     for element in mo:
#         if element[0] == '+' or element[0] == '':
#             if element[1] == '':
#                 polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) + 1
#             else:
#                 polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) + int(element[1])
#         else:
#             if element[1] == '':
#                 polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) - 1
#             else:
#                 polyDict[''.join(sorted(element[2]))] = polyDict.get(''.join(sorted(element[2])), 0) - int(element[1])
#     for key in sorted(polyDict):
#         alphaSortDict[key] = polyDict[key]
#     for key in sorted(alphaSortDict, key=len):
#         digitSortDict[key] = alphaSortDict[key]
#     for key, value in digitSortDict.items():
#         if value < -1:
#             lst.append(str(value)+key)
#         elif value == -1:
#             lst.append('-'+key)
#         elif value == 0:
#             continue
#         elif value == 1:
#             lst.append('+'+key)
#         else:
#             lst.append('+'+str(value)+key)
#     return ''.join(lst).lstrip('+') 



import re
def simplify(poly):
    p = {}
    for m in re.findall(r'([+-]?)(\d*)([a-z]+)', poly):
        var = ''.join(sorted(m[2]))
        p[var] = p.get(var,0)+(-1 if m[0]=='-' else 1)*(int(m[1]) if m[1]!='' else 1)
    poly = ''.join('+-'[p[k]<0]+str(abs(p[k]))+k for k in sorted(p, key=lambda x:(len(x),x)) if p[k])
    return re.sub('([+-])1(?=[a-z])',r'\1', poly)[poly[0]=='+':]
