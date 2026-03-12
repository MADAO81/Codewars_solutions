# https://www.codewars.com/kata/593b1909e68ff627c9000186/train/python

# def nickname_generator(name):
#     if len(name)<4:
#         return "Error: Name too short"
#     vowels = 'aeiou'
#     if name[2] in vowels:
#         return name[:4]
#     else:
#         return name[:3]
    

def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3+(name[2] in "aeiuo")]
