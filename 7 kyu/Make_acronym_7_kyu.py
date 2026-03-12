# https://www.codewars.com/kata/57a60bad72292d3e93000a5a/train/python

# def to_acronym(inp):
#     inp = inp.split()
#     result = []
#     for word in inp:
#         result.append(word[0].upper())
#     return ''.join(result)


# def to_acronym(input):
#   return ''.join(w[0].upper() for w in input.split())


def to_acronym(input):
  return ''.join(word[0] for word in input.split()).upper()
