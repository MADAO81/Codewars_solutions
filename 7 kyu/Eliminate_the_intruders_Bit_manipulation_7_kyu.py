# https://www.codewars.com/kata/5a0d38c9697598b67a000041/train/python

# def eliminate_unset_bits(number):
#     result = number.replace('0','')
#     if not result:
#         return 0
#     return int(result,2)


# def eliminate_unset_bits(number):
#     return int( "0" + number.replace("0", ""), 2

               

def eliminate_unset_bits(string):
    return 2 ** (string.count('1')) - 1


