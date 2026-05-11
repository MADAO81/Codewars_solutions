# https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/python

# Solution_1
# give_change = lambda x: (x % 5, x % 10 // 5, x % 50 % 20 // 10, x % 50 // 20, x % 100 // 50, x // 100)

# Solution_2

def give_change( money ):
    arr = []
    for i in [100, 50, 20, 10, 5, 1]:
        arr = [money // i] + arr
        money -= arr[0] * i
    return tuple(arr)
