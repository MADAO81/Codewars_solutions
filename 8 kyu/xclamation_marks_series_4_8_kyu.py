# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. 
# For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

# Examples
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!"
# "!Hi"     ---> "Hi!"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi!"

# def remove(st):
#     result = []
#     for ch in st:
#         if ch != "!":
#             result.append(ch)
#     result.append("!")
#     return "".join(result)

def remove(s):
    return s.replace("!", "") + "!"
