# https://www.codewars.com/kata/58373ba351e3b615de0001c3/train/python


# def mormons(starting_number, reach, target):
#     missions = 0
#     while starting_number < target:
#         starting_number *= (1 + reach)
#         missions += 1
#     return missions



def mormons(starting_number, reach, target):
    if starting_number >= target:
        return 0
    return 1 + mormons(starting_number * (1 + reach), reach, target)


