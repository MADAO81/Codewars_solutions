# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# N	Product	N factorial	Trailing zeros
# 6	1*2*3*4*5*6	720	1
# 12	1*2*3*4*5*6*7*8*9*10*11*12	479001600	2
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.




# def zeros(n):
#     """
#     No factorial is going to have fewer zeros than the factorial of a smaller
#     number.

#     Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
#     smaller than `n` (`n // 5`).

#     Each multiple of 25 adds two 0's, so next we add another 0 for each multiple
#     of 25 smaller than n.

#     We continue on for all powers of 5 smaller than (or equal to) n.
#     """
#     pow_of_5 = 5
#     zeros = 0
    
#     while n >= pow_of_5:
#         zeros += n // pow_of_5
#         pow_of_5 *= 5
        
#     return zero

def zeros(n):
    result = 0
    degree = 1
    
    while n>0 and n/(5**degree) >= 1:
        result += int(n/5**degree)
        degree += 1
    return result
