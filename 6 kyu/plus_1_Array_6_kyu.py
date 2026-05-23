# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# If the array is invalid (empty, or contains negative integers or integers with more than 1 digit), return nil (or your language's equivalent).

# Examples
# Valid arrays

# [4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
# [1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
# [0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)
# Invalid arrays

# [] is invalid because it is empty
# [1, -9] is invalid because -9 is not a non-negative integer
# [1, 2, 33] is invalid because 33 is not a single-digit integer


# def up_array(arr):
    
#     if not arr or min(arr) < 0 or max(arr) > 9:
#         return None
    
#     for i in range(len(arr)-1,-1,-1):
#         arr[i] += 1 
#         if arr[i] < 10: return arr
#         else: arr[i] = 0
        
#     return [1]+arr

# def up_array(arr):
#     if not arr:
#         return None
    
#     for i in arr:
#         if i < 0 or i > 9:
#             return None

#     result = "".join(map(str, arr))
#     result = int(result) + 1
#     result = list(map(int, str(result)))
    
#     if not arr[0] and len(arr) > 1:
#         result.insert(0, 0)
    
#     return result

def up_array(a):
    if not a or any(not 0 <= x < 10 for x in a): return
    for i in range(1, len(a)+1):
        a[-i] = (a[-i] + 1) % 10
        if a[-i]: break
    else: a[:0] = [1]
    return a
