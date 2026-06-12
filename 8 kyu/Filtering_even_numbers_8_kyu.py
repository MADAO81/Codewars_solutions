# Filtering even numbers (Bug Fixes)
# The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

# However, there is a bug in the method that needs to be resolved.

def kata_13_december(lst): 
    # Fix this code
    result = []
    for i in lst: 
        if i % 2 != 0: 
            result.append(i)
    return result
