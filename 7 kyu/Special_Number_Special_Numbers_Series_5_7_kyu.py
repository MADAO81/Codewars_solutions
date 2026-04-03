# https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python

# SPECIAL = set('012345')

# def special_number(number):
#     return "Special!!" if set(str(number)) <= SPECIAL else "NOT!!"


def special_number(number):
    if max(str(number))<="5":
        return "Special!!"
    else:
        return "NOT!!"
