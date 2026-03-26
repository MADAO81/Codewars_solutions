# https://www.codewars.com/kata/56576f82ab83ee8268000059/train/python

# def spacey(array):
#     result = []
#     combined_word = ''
#     for word in array:
#         combined_word += word
#         result.append(combined_word)
#     return result


def spacey(array):
    return [''.join(array[:i+1]) for i in range(len(array))]
