# Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

# Notes :
# Array/list size is at least 3 .

# Array/list numbers could be a mixture of positives , negatives and zeros .

# Repetition of numbers in the array/li

# def max_tri_sum(numbers):
#     numbers = sorted(list(set(numbers)))
#     return numbers[-1] + numbers[-2] + numbers[-3]

def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])
