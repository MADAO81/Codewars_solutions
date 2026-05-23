# https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python

# def capitals_first(text):
#     t1, t2 = [], []  
#     for word in text.split():
#         if word and word[0].isupper():  
#             t1.append(word)
#         elif word and word[0].islower(): 
#             t2.append(word)
#     return " ".join(t1 + t2)

def capitals_first(text):
    uppers = [word for word in text.split() if word[0].isupper()]
    lowers = [word for word in text.split() if word[0].islower()]
    return " ".join(uppers + lowers)
    
