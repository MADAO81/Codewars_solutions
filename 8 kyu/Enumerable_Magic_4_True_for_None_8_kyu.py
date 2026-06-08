# Enumerable Magic #4 - True for None?
# Write a function that takes two arguments: an array and a callback function (in Ruby: a block).

# The function should return true if the callback / block returns false for all of the items in the array, or if the array is empty; otherwise return false.

def none(lst, func):
    return not any(func(x) for x in lst)
