# Thinking & Testing : Retention and discard
# No Story

# No Description

# Only by Thinking and Testing

# Look at the results of the testcases, and guess the code!

def mystery(n):
    result = []
    i = 1
    while i <= n:
        if n % i == 0:
            result.append(i)
        i +=2
    return result
