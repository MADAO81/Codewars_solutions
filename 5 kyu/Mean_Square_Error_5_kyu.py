# Mean Square Error
# Complete the function that
# -accepts two integer arrays of equal length
# -compares the value each member in one array to the corresponding member in the other
# -squares the absolute value difference between those two values
# -and returns the average of those squared absolute value difference between each member pair.


# def solution(a, b):
#     return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

# def solution(a, b):
#     return sum((a[i]-b[i])**2 for i in range(len(a)))/len(a)


def solution(array_a, array_b):
    sum_of_squares = 0
    result = 0
    for i in range(len(array_a)):
        (array_a[i]-array_b[i])**2
        sum_of_squares += (array_a[i]-array_b[i])**2
    result = sum_of_squares / len(array_a)
    return result
