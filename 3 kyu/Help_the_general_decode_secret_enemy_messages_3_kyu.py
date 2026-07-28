# https://www.codewars.com/kata/52cf02cd825aef67070008fa/train/python

# def decode(s):
#     result = ""
#     # Добавляем все необходимые символы: запятая, точка, вопросительный знак и т.д.
#     all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-.,?"
    
#     for i, ch in enumerate(s):
#         found = False
#         for test_char in all_chars:
#             try:
#                 filler = "_" * i
#                 enc = encode(filler + test_char)
#                 if len(enc) > i and enc[i] == ch:
#                     result += test_char
#                     found = True
#                     break
#             except:
#                 pass
        
#         if not found:
#             result += ch
    
#     return result

def decode(s):
    decrypted_message = ''
    i = 0
    key = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"

    for char in s:
        i += 1
        if char not in key:
            decrypted_message += char
            continue
            
        idx = (key.index(char) - i) % 66
        decrypted_message += key[idx]
        
    return decrypted_message
