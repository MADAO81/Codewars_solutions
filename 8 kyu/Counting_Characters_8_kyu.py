# Define a method named countCharOccurrences or count_char_occurrences that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int.

# def count_char_occurrences(strng, char):
#     count = 0
#     for ch in strng:
#         if ch == char:
#             count +=1
#     return count

def count_char_occurrences(strng, char):
    return strng.count(char)

