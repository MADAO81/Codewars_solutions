# https://www.codewars.com/kata/57ef016a7b45ef647a00002d/train/python

# def filter_homogenous(arrays):
#     filtered = [ 
#         row for row in arrays
#         if row and all(type(item) is type(row[0]) for item in row)]
#     return filtered



# def filter_homogenous(arrays):
#     return [a for a in arrays if a and all(type(a[0]) == type(b) for b in a)]


def filter_homogenous(arrays):
    return[a for a in arrays if len(set(map(type,a)))==1]
