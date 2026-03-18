# Product Array (Array Series #5)
# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

# Notes
# Array/list size is at least 2 .

# Array/list's numbers Will be only Positives

# Repetition of numbers in the array/list could occur.

# Input >> Output Examples
# productArray ({12,20}) ==>  return {20,12}
# Explanation:
# The first element in prod [] array 20 is the product of all array's elements except the first element

# The second element 12 is the product of all array's elements except the second element .

# productArray ({1,5,2}) ==> return {10,2,5}
# Explanation:
# The first element 10 is the product of all array's elements except the first element 1

# The second element 2 is the product of all array's elements except the second element 5

# The Third element 5 is the product of all array's elements except the Third element 2.



# from operator import mul
# from functools import reduce

# def product_array(numbers):
#     total = reduce(mul,numbers)
#     return [total//n for n in numbers]


# from math import prod
# def product_array(numbers):
#     return [prod(numbers)/i for i in numbers]


def product_array(numbers):
    p = 1
    for el in numbers:
        p *= el
    return [p / el for el in numbers]
