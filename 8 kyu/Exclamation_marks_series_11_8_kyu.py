# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
# Description:
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

# Examples
# "Hi!" --> "H!!"
# "!Hi! Hi!" --> "!H!! H!!"
# "aeiou" --> "!!!!!"
# "ABCDE" --> "!BCD!"


# def replace_exclamation(st):
#     vowel_str = "aeiouAEIOU"
#     result = []
#     for ch in st:
#         if ch  in vowel_str:
#             result.append("!")
#         else:
#             result.append(ch)
            
#     return "".join(result)



def replace_exclamation(st):
    return ''.join('!' if letter in 'aeiouAEIOU' else letter for letter in st)
