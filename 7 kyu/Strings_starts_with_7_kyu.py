# https://www.codewars.com/kata/5803a6d8db07c59fff00015f/train/python

# def starts_with(st, prefix): 
#     if prefix == '':
#         return True
#     elif len(prefix) > len(st):
#         return False
#     elif prefix in st and prefix[0] == st[0]:
#         return True
#     else:
#         return False



# def starts_with(s, prefix): 
#     return s[:len(prefix)]==prefix



def starts_with(st, prefix): 
    return st.startswith(prefix)
