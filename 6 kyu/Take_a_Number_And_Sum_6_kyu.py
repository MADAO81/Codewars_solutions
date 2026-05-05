# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python



# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     result = []
#     for x in range(a, b+1):
#         char = []
#         n = 0
#         for i in str(x):
#             char.append(int(i) ** (n+1))
#             n += 1
#         if x == sum(char):
#             result.append(x)
#     return result



def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]
