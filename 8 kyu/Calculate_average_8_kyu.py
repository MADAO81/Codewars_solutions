# Calculate average
# Write a function which calculates the average of the numbers in a given array.
# Note: Empty arrays should return 0.



# from statistics import mean
# def find_average(numbers):
#     try:
#         return mean(numbers)
#     except:
#         return 0

# def find_average(numbers):
#     if len(numbers) > 0:
#         return sum(numbers)/len(numbers)
#     else:
#         return 0



import statistics

def find_average(numbers):
    if len(numbers) > 0:
        return statistics.mean(numbers)
    else:
        return 0
