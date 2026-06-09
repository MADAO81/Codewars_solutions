# Exclamation marks series #1: Remove an exclamation mark from the end of string
# Description:
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi!!"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"



# def remove(s):
#     if len(s)==0:
#         return s
#     if s[-1] == "!":
#         return s[:-1]
#     return s



def remove(s):
    return s[:-1] if s.endswith('!') else s
