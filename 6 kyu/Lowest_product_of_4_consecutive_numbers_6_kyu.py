# https://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python

# def lowest_product(num):
#     if len(num)<4:
#         return "Number is too small"
#     min_product = int(num[0])*int(num[1])*int(num[2])*int(num[3])
#     for i in range(len(num)-3):
#         product = int(num[i])*int(num[i+1])*int(num[i+2])*int(num[i+3])
#         if product < min_product:
#             min_product = product
#     return min_product



# from operator import mul
# from functools import reduce # python 3 support

# def lowest_product(input):
#     if len(input) < 4: return "Number is too small"
#     return min([reduce(mul, map(int, input[i:i+4])) for i in range(len(input)-3)])



def lowest_product(input):
    length = len(input)
    
    if length < 4:
        return "Number is too small"
    
    def muller(fourchar):
        prod = 1
        for num in fourchar:
            prod *= int(num)
        return prod
        
    return min([muller(input[i:i+4]) for i in range(length-3)])
