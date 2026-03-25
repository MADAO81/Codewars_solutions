# Thinking & Testing : Incomplete string
# No Story

# No Description

# Only by Thinking and Testing

# Look at result of testcase, guess the code!



# import re

# def testit(s):
#     return re.sub("(.)(.)", lambda m: chr((ord(m[1]) + ord(m[2])) // 2), s)


def testit(s):
    arr = [chr((ord(s[i]) + ord(s[i+1]))//2) for i in range(0,len(s)-1,2)]
    return "".join(arr) if len(s) % 2 == 0 else "".join(arr) + s[-1]
    
