# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python


# land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2

# def land_perimeter(a):
#     return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))



def land_perimeter(arr):
    total_perimeter = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == "X":
                total_perimeter += 4
                if (x != len(arr) - 1) and (arr[x + 1][y] == 'X'):
                    total_perimeter -= 1
                if (x != 0) and (arr[x - 1][y] == 'X'):
                    total_perimeter -= 1
                if (y != len(arr[0]) - 1) and (arr[x][y + 1] == 'X'):
                    total_perimeter -= 1
                if (y != 0) and (arr[x][y - 1] == 'X'):
                    total_perimeter -= 1
    return f"Total land perimeter: {total_perimeter}"
