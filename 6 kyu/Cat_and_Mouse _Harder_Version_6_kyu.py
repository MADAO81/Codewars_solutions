# https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf/train/python

# def cat_mouse(x,j):
#     idxs = {a: i for i, a in enumerate(x)}
#     cat = idxs.get('C')
#     dog = idxs.get('D')
#     mouse = idxs.get('m')
#     if cat is None or dog is None or mouse is None:
#         return 'boring without all three'
#     elif abs(cat - mouse) <=j + 1:
#         if cat < dog < mouse or mouse < dog < cat:
#             return 'Protected!'
#         return 'Caught!'
#     return 'Escaped!'


def cat_mouse(x,j):
    d, c, m = x.find('D'), x.find('C'), x.find('m')
    if -1 in [d, c, m]:
        return 'boring without all three'
    if abs(c - m) <= j:
        return 'Protected!' if c < d < m or m < d < c else 'Caught!' 
    return 'Escaped!'
