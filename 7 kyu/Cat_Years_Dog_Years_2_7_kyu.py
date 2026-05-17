# https://www.codewars.com/kata/5a6d3bd238f80014a2000187/train/python

def owned_cat_and_dog(cy, dy):
    cat = 0 if cy < 15 else 1 if cy < 24 else 2 + (cy - 24) // 4
    dog = 0 if dy < 15 else 1 if dy < 24 else 2 + (dy - 24) // 5
    return [cat, dog]
