# Return Two Highest Values in List
# In this kata, your job is to return the two distinct highest values in a list. 
# If there're less than 2 unique values, return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

# def two_highest(arg1):
#     step1 = set(arg1)
#     step2 = sorted(list(step1), reverse = True)
#     return step2[:2]
    
def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]
