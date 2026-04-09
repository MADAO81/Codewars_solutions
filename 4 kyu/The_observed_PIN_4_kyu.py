# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

# import itertools
# def get_pins(observed):
#     adj = {"1":["2","4"], "2":["1","3","5"], "3":["2","6"], "4":["1","5","7"],
#           "5":["2","4","6","8"], "6":["3","5","9"], "7":["4","8"], "8":["5","7","9","0"],
#           "9":["6","8"], "0":["8"]}
#     l = [[digit]+adj[digit] for digit in observed]
#     return ["".join(element) for element in list(itertools.product(*l))]


# def get_pins(observed):
#     adj = {
#         "1": "124",
#         "2": "2135",
#         "3": "326",
#         "4": "4157",
#         "5": "52468",
#         "6": "6359",
#         "7": "748",
#         "8": "85790",
#         "9": "968",
#         "0": "08",
#     }
#     result = ['']
#     for d in observed:
#         result = [prefix+c for prefix in result for c in adj[d]]
#     return result

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
