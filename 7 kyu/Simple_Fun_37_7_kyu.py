# https://www.codewars.com/kata/58880c6e79a0a3e459000004/train/python

# def house_numbers_sum(inp):
#     return sum(inp[:inp.index(0)])

def house_numbers_sum(inp):
    result = 0
    for number in inp:
        if number !=0:
            result += number
        else:
            break
    return result
