# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python


# from collections import Counter

# def number_of_pairs(gloves):
#     return sum(ch//2 for ch in Counter(gloves).values())


# def number_of_pairs(gloves):
#     unique = set(gloves)
#     return sum(gloves.count(i)//2 for i in unique)



def number_of_pairs(gloves):
    return sum(gloves.count(color)//2 for color in set(gloves))
