# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python


# def recoverSecret(triplets):
#     res = ''
#     while triplets != []:
#         non_firsts = [num for t in triplets for num in t[1:]]
#         firsts = [t[0] for t in triplets]
#         for f in firsts:
#             if f not in non_firsts:
#                 res += f
#                 for t in triplets:
#                     if t[0] == f:
#                         t.pop(0)
#                 break
#         triplets = [t for t in triplets if t != []]
#     return res

def recoverSecret(triplets):
    letters = list(set([l for t in triplets for l in t]))        
            
    for t in triplets * len(letters):
        for i in range(len(t)-1):
            a, b = letters.index(t[i]), letters.index(t[i+1])
            if( a > b ): letters[b], letters[a] = letters[a], letters[b]
            
    return ''.join(letters)
