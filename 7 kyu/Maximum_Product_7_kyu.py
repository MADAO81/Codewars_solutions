# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python

# def adjacent_element_product(array):
#     max_prod = -float("inf")  # Initialize with negative infinity to handle negative products
#     for i in range(len(array) -1):
#         current_prod = array[i]*array[i+1]
#         if current_prod > max_prod:
#             max_prod = current_prod
#     return max_prod

def adjacent_element_product(array):
    return max( a*b for a, b in zip(array, array[1:]) )
