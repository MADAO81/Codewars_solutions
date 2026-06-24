# https://www.codewars.com/kata/56cac350145912e68b0006f0/train/python

# def arrange(s):
#     words = s.split()
#     n = len(words)
    
#     changed = True
#     while changed:
#         changed = False
#         i = 0
#         while i < n - 1:

#             if i % 2 == 0:
#                 if len(words[i]) > len(words[i + 1]):
#                     words[i], words[i + 1] = words[i + 1], words[i]
#                     changed = True
#                     if i > 0:
#                         i -= 1
#                         continue

#             else:
#                 if len(words[i]) < len(words[i + 1]):
#                     words[i], words[i + 1] = words[i + 1], words[i]
#                     changed = True
#                     if i > 0:
#                         i -= 1
#                         continue
#             i += 1

#     return ' '.join(w.lower() if i % 2 == 0 else w.upper() 
#                     for i, w in enumerate(words))


def arrange(strng):
    words = strng.split()
    for i in range(len(words)):
        words[i:i+2] = sorted(words[i:i+2], key=len, reverse=i%2)
        words[i] = words[i].upper() if i%2 else words[i].lower()
    return ' '.join(words)
