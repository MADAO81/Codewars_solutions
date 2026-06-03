# Find the length of the longest substring in the given string s that is the same in reverse.

# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

# If the length of the input string is 0, the return value must be 0.

# Example:
# "a" -> 1 
# "aab" -> 2  
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0

# def longest_palindrome (s):
#     lst = enumerate(s)
#     word = ""
#     tmp = []
#     if len(s) == 1:
#         return 1
#     elif len(s) == 0:
#         return 0
#     else:
#         for item, value in lst:
#             c = 1
#             for i in range(item):
#                 word = s[i:item+1]
#                 if word == word[::-1]:
#                     tmp.append(len(word))
                    
#     if len(tmp) == 0:
#         return 1
#     else:
#         return max(tmp)


def longest_palindrome (s):

  longest = 0

  for j in range(1, len(s)+1):
    for i in range(j):
      t = s[i:j]
      if t == t[::-1]:
        longest = max(longest, len(t))
  
  return longest
