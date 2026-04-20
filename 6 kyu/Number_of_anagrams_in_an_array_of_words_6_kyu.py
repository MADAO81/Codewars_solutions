# An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters. An example of this is "angel", which is an anagram of "glean".

# Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words inside it.

# Some examples:

# There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
# There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]

# from collections import Counter
# import math
# def choose(n, k):  
#     f = math.factorial
#     return (f(n)//(f(n-k)*f(k)))

# def anagram_counter(words):
#     count = Counter(frozenset(Counter(word).items()) for word in words)
#     return sum(choose(x,2) for x in count.values() if x >1)



# def anagram_counter(words):
#     total = 0
#     for i, word in enumerate(words[:-1]):
#         letters = sorted([*word])
#         for other_word in words[i+1:]:
#             if sorted([*other_word]) == letters:
#                 total +=1
#     return total


from collections import Counter

def anagram_counter(words):
    return sum(n*(n-1)// 2 for n in Counter(''.join(sorted(x)) for x in words).values())
