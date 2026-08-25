# https://www.codewars.com/kata/56a1c63f3bc6827e13000006/train/python

def smaller(arr):
    if not arr:
        return []
    
    # Coordinate compression: map each value to its rank
    # We need to handle duplicates carefully
    sorted_unique = sorted(set(arr))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}  # 1-based indexing for BIT
    
    # Fenwick tree (Binary Indexed Tree)
    size = len(sorted_unique)
    bit = [0] * (size + 1)
    
    def update(idx, val):
        while idx <= size:
            bit[idx] += val
            idx += idx & -idx
    
    def query(idx):
        # Returns sum from 1 to idx
        result = 0
        while idx > 0:
            result += bit[idx]
            idx -= idx & -idx
        return result
    
    result = [0] * len(arr)
    
    # Process from right to left
    for i in range(len(arr) - 1, -1, -1):
        rank = rank_map[arr[i]]
        # Count how many numbers we've seen that are smaller than current
        # (i.e., with rank < current rank)
        result[i] = query(rank - 1)
        # Add current number to BIT
        update(rank, 1)
    
    return result
