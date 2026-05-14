# Reverse every other word in a given string, then return the string. 
# Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
# Punctuation marks should be treated as if they are a part of the word in this kata.


# def reverse_alternate(st):
#     st = st.split()
#     result = []
#     for i, word in enumerate(st):
#         if i%2 !=0:
#             result.append(word[::-1])
#         else:
#             result.append(word)
#     return " ".join(result)


# def reverse_alternate(s):
#     return " ".join(map(lambda x:(x[1][::-1],x[1])[x[0]%2],enumerate(s.strip().split(),1)))  



def reverse_alternate(string):
    return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))
