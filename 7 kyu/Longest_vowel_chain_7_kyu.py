# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. 
# Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. 
# Vowels are any of aeiou.

# import re
# def solve(s):
#     matches = re.findall('[aeiou]+', s)
#     if not matches:
#         return 0
#     else:
#         return len(max(matches, key=len))


import re
def solve(s):
  return len(max(re.findall(r"[aeiou]+", s), key=len, default=""))
