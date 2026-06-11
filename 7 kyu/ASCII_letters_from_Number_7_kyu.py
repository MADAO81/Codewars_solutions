# https://www.codewars.com/kata/589ebcb9926baae92e000001/train/python

# def convert(number_string):
#     result = []    
#     for i in range(0, len(number_string), 2):
#         ascii_code = int(number_string[i:i+2])        
#         if ascii_code == 32:
#             result.append(' ')     
#         elif 65 <= ascii_code <= 90:
#             result.append(chr(ascii_code))  
#         else:
#             result.append('?')    
#     return ''.join(result)


def convert(number):
    return ''.join(chr(int(number[a:a + 2])) for a in range(0, len(number), 2))
