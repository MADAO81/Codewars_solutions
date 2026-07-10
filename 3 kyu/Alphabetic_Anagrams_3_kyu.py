# https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python

# from math import factorial
# from collections import Counter

# def list_position(word):

#     freq = Counter(word)
#     n = len(word)
    
#     fact = [1] * (n + 1)
#     for i in range(2, n + 1):
#         fact[i] = fact[i - 1] * i
    
#     rank = 1
    
#     for i, char in enumerate(word):

#         for smaller_char in sorted(freq.keys()):
#             if smaller_char >= char:
#                 break
#             if freq[smaller_char] == 0:
#                 continue
                

#             freq[smaller_char] -= 1
            
#             remaining = n - i - 1
#             perms = fact[remaining]

#             for count in freq.values():
#                 perms //= fact[count]
            
#             rank += perms
            
#             # Возвращаем букву обратно
#             freq[smaller_char] += 1

#         freq[char] -= 1
#         if freq[char] == 0:
#             del freq[char]
    
#     return rank



from collections import Counter

def listPosition(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        for y in c:
            if (y < x):
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r
