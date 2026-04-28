# https://www.codewars.com/kata/55cb0597e12e896ab6000099/train/python

# def arithmetic_sequence_sum(a, r, n):
#     result = 0
#     for i in range(n):
#         result = result + a + (r*(i))
#     return result



# def arithmetic_sequence_sum(a, r, n):
#     return sum(a + r*x for x in range(n))



def arithmetic_sequence_sum(a, r, n):
    return n * (a + a + ( n - 1) * r) / 2  
