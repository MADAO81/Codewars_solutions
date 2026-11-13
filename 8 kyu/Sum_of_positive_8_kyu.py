# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    sum_of_positive = 0
    for i in arr:
        if i >0:
            sum_of_positive +=i
            
    return sum_of_positive
