# https://www.codewars.com/kata/56bf3287b5106eb10f000899/train/python

# def move_vowels(input): 
#     vowels = "aeiouAEIOU"
#     find_vowels = ''.join([char for char in input if char in vowels])
#     find_others = ''.join([char for char in input if char not in vowels])
#     return find_others+find_vowels


# def move_vowels(i): 
#     s, v = '', ''
#     for letter in i:
#         if letter in 'aeiou': v+=letter
#         else: s+=letter
#     return s+v



def move_vowels(s): 
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))

