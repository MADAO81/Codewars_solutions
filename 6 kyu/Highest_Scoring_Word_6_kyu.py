# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def high(x):
    words = x.split()
    greatest_word = ""
    greatest_rating = 0
    value = 0
    for word in words:
        value = word_rating(word)
        if value > greatest_rating:
            greatest_rating = value
            greatest_word = word
    return greatest_word
        
    
def word_rating(word):
    return sum([ord(w) - 96 for w in word])
