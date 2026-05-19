# https://www.codewars.com/kata/559536379512a64472000053/train/python

# def play_pass(s, n):
#     result = ''
#     for ch in map(ord, s):
#         if ch in range(65,91):
#             result += chr((((ch-65) + n) % 26) + 65)
#         elif ch in range(97, 123):
#             result += chr(((((ch-97) + n) % 26) + 97))
#         elif ch in range(48,58):
#             result += str(abs(9 - int(chr(ch))))
#         else:
#             result += str(chr(ch))
#     result = ''.join([result[i].upper() if i % 2 == 0 else result[i].lower() for i in range(len(result))])
#     return result[::-1]

def play_pass(s, n):

    # Step 1, 2, 3
    shiftText = ""
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char

    # Step 4
    caseText = ""
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()

    # Step 5
    return caseText[::-1]
