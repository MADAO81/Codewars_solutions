# https://www.codewars.com/kata/558878ab7591c911a4000007/train/python


# def pig_latin(s):
#     if not s.isalpha():
#         return None
#     s = s.lower()
#     vowels = 'aeiou'
#     first_vowel_index = -1
#     for i,char in enumerate(s):
#         if char in vowels:
#             first_vowel_index = i
#             break
#     if first_vowel_index == -1:
#         return s + 'ay'
#     if first_vowel_index == 0:
#         return s + 'way'
#     consonants = s[:first_vowel_index]
#     rest = s[first_vowel_index:]
#     return rest+consonants+'ay'


def pig_latin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = s.lower()
    if not word.isalpha():    # Check for non alpha character
        return None
    if word[0] in vowels:     # Check if word starts with a vowel
        return word + 'way'
    for i, letter in enumerate(word):    # Find the first vowel and add the beginning to the end 
        if letter in vowels:
            return word[i:]+word[:i]+'ay'
    return word + 'ay'    # No vowels
