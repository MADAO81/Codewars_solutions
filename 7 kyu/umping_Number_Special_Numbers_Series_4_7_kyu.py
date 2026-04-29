# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

# def jumping_number(number):
#     number = list(str(number))
#     for i in range(0,len(number)-1):
#         if abs(int(number[i+1])-int(number[i])) !=1:
#             return "Not!!"
#     return "Jumping!!"


def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]
