# https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/python

# def mirror(data: list) -> list:
#     x = sorted(data)
#     y = x[::-1][1:]
#     return x+y


# def mirror(data):
#     return (s := sorted(data)) + s[-2::-1]



def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]
