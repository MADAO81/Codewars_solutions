# Sort and Star
# You will be given a list of strings. 
# You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) 
# and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.

# def two_sort(array):
#     result = sorted(array)[0]
#     return "***".join(list(result))
    

def two_sort(array):
    return '***'.join(min(array))
