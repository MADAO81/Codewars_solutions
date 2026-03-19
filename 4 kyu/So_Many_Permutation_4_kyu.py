# So Many Permutations!
# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

# Create as many "shufflings" as you can!

# Examples:

# With input 'a':
# Your function should return: ['a']

# With input 'ab':
# Your function should return ['ab', 'ba']

# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']

# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.


# Solution_1
# def permutations(s):
#     result = set([s])
#     if len(s) == 2:
#         result.add(s[1] + s[0])
#     elif len(s) > 2:
#         for i, c in enumerate(s):
#             for t in permutations(s[:i] + s[i + 1:]):
#                 result.add(c + t)
#     return result


# Solution_2
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))
