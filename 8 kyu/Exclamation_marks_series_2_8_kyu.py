# Exclamation marks series #2: Remove all exclamation marks from the end of sentence

# Description:
# Remove all exclamation marks from the end of sentence.

# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"

def remove(st):
    return st.rstrip("!")
