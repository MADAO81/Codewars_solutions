# https://www.codewars.com/kata/57faefc42b531482d5000123/train/python

# def remove(s):
#     clean_part = s.rstrip('!')
#     tail = s[len(clean_part):]
#     result = clean_part.replace('!','')+tail
#     return result



# import re

# def remove(s):
#     return re.sub(r'!+(?!!*$)', '', s)



def remove(s):
    return s.replace('!', '')+ '!'*(len(s)- len(s.rstrip('!')))
