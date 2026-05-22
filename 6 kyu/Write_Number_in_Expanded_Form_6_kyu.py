# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.



# def expanded_form(num):
#     result = []
#     for index, digit in enumerate(str(num)[::-1]):
#         if int(digit) !=0:
#             result.append(digit + ("0"*index))
#     return " + ".join(result[::-1])


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
