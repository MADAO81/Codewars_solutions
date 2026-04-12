# Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

# For example: (Input --> Output)

# 10 --> 1
# 99 --> 18
# -32 --> 5
# Let's assume that all numbers in the input will be integer values.


# def sum_digits(number):
#     number = abs(number)
#     result = 0
#     while number > 0:
#         result += number % 10
#         number //= 10
#     return result

# def sum_digits(number):
#     number = abs(number)
#     result = 0
#     for i in str(number):
#         result += int(i)
#     return result
  
def sum_digits(number):
    return sum(map(int, str(abs(number))))
