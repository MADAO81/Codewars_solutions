# https://www.codewars.com/kata/559a28007caad2ac4e000083/solutions/python


# def perimeter(n):
#     a = 0
#     b = 1
#     total = 0
#     for i in range(n+1):
#         total += b
#         a,b = b,a+b
#     return total*4


def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b 
        else:
            a, b = b, a+b
            yield b
        

def perimeter(n):
    return sum(fib(n)) * 4
