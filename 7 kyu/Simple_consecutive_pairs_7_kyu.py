# In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:

# pairs([1,2,5,8,-4,-3,7,6,5]) = 3
# The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
# --the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
# --the second pair is (5,8) and are not consecutive
# --the third pair is (-4,-3), consecutive. Count = 2
# --the fourth pair is (7,6), also consecutive. Count = 3. 
# --the last digit has no pair, so we ignore.
# More examples in the test cases.


# def pairs(arr):
#     return sum( abs(a-b)==1 for a,b in zip(arr[::2],arr[1::2]) )


def pairs(arr):
    total = 0
    for i in range(0, len(arr)-1,2):
        if abs(arr[i]-arr[i+1]) == 1:
            total += 1
    return total
