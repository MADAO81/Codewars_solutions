# https://www.codewars.com/kata/58039f8efca342e4f0000023/train/python

# def changer(s):
#     """
#     Transforms a string by:
#     1. Replacing every letter with the next letter in the alphabet (wrapping Z to A)
#     2. Making vowels uppercase
#     3. Making consonants lowercase
    
#     Args:
#         s: Input string
    
#     Returns:
#         Transformed string
#     """
#     result = []
#     for char in s:
#         # Check if the character is a letter
#         if char.isalpha():
#             # Step 1: Replace with next letter (case-insensitive)
#             if char.isupper():
#                 next_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
#             else:
#                 next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            
#             # Step 2 & 3: Adjust case based on whether it's a vowel
#             # Vowels: A, E, I, O, U (y is not considered a vowel)
#             if next_char.upper() in 'AEIOU':
#                 result.append(next_char.upper())
#             else:
#                 result.append(next_char.lower())
#         else:
#             # Non-letters remain unchanged
#             result.append(char)
    
#     return ''.join(result)

def changer(s):
    return s.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA'))
