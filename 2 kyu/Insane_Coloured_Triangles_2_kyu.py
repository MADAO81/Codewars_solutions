# https://www.codewars.com/kata/5a331ea7ee1aae8f24000175/train/python

# good_numbers = [1, 4, 10, 28, 82, 244, 730, 2188, 6562, 19684, 59050, 177148]

# colors = set('RGB')


# def simple_solve(guys):
#     while len(guys) > 1:
#         guys = [a if a == b else (colors-{a, b}).pop() for a, b in zip(guys, guys[1:])]
#     return guys[0]


# def closest_good_number(number, good_numbers):
#     closest = sorted(good_numbers, key=lambda x: abs(x - number))
#     for value in closest:
#         if value <= number:
#             return value


# def sides_until_good(guys):

#     if len(guys) < 4:
#         return simple_solve(guys)

#     good_number = closest_good_number(len(guys), good_numbers)
#     size = len(guys) - good_number + 1

#     left = guys[:size]
#     right = guys[-size:]


#     a = sides_until_good(left)
#     b = sides_until_good(right)
#     final = simple_solve((a, b))

#     return final


def triangle(row):

    def reduce(a, b):
        return a if a == b else (set('RGB') - {a , b}).pop()

    def walk(offset, root, depth):
        return row[root] if not depth else curry(offset, root, *divmod(depth, 3))

    def curry(offset, root, depth, degree):
        return walk(3 * offset, root, depth) if not degree \
            else reduce(curry(offset, root, depth, degree - 1), curry(offset, root + offset, depth, degree - 1))

    return walk(1, 0, len(row) - 1)


def triangle(input):
    guy = sides_until_good(input)
    return guy
