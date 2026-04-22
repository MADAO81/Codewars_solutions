# Two to One
# Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string (alphabetical ascending), the longest possible, 
# containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    semifinal = ""
    final = ""
    result = a1+a2
    result_set = set(result)
    for ch in result_set:
        semifinal +=ch
    semifinal = sorted(semifinal)
    for letter in semifinal:
        final += letter
    return final
    
    
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
