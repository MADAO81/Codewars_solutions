# https://www.codewars.com/kata/58ff1c8b13b001a5a50005b4/train/python

# def sort_animals(lst : list) -> list:
#     return sorted(lst, key = lambda animal: (animal.number_of_legs, animal.name))


def sort_animals(input):
    return sorted(input, key = lambda x: (x.number_of_legs, x.name))
