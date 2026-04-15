# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

# Example:

# Input:

# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

# Output:

# 'alpha beta gamma delta'



# def remove_duplicate_words(s):
#     result = []
#     for word in s.split():
#         if word not in result:
#             result.append(word)
#     return " ".join(result)



def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))
