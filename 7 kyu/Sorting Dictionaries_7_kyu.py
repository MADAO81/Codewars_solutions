# https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python

# def sort_dict(d):
#     'return a sorted list of tuples from the dictionary'
#     new_d = sorted(d.items(), reverse=True, key=lambda x: x[1])
#     return new_d


def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)
