# Scrabble Score
# Write a program that, given a word, computes the scrabble score for that word.

# Letter Values
# You'll need these:

# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10
# There will be a preloaded dictionary dict_scores with all these values: dict_scores["E"] == 1



# def scrabble_score(st): 
#     values = {"aeioulnrst": 1, "dg": 2, "bcmp": 3, "fhvwy": 4, "k": 5, "jx": 8, "qz": 10}
#     score = 0
#     for letter in st:
#         for key, value in values.items():
#             if letter.lower() in key:
#                 score += value
#     return score


def scrabble_score(st): 
    return sum(dict_scores.get(letter,0) for letter in st.upper())
