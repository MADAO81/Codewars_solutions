# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python

# def work_on_strings(a,b):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     switch_a = []
#     switch_b = []
#     for letter in alphabet:
#         switch_a.append(b.lower().count(letter)%2)
#         switch_b.append(a.lower().count(letter)%2)
#     concat = a + b
#     output = ''
#     for i,letter in enumerate(concat):
#         if i < len(a):
#             if switch_a[alphabet.index(letter.lower())] == 1:
#                 letter = letter.swapcase()
#         else:
#             if switch_b[alphabet.index(letter.lower())] == 1:
#                 letter = letter.swapcase()
#         output += letter
#     return output



# from collections import Counter

# def swap_them(a, b):
#     cnt = Counter(b.lower())
#     return "".join(c.swapcase() if cnt[c.lower()] % 2 else c for c in a)

# def work_on_strings(a, b):
#     return swap_them(a, b) + swap_them(b, a)



def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)
