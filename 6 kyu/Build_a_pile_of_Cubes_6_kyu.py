# see https://www.codewars.com/kata/5592e3bd57b64d00f3000047/solutions/python





# def find_nb(m):
#     n = 1
#     volume = 0
#     while volume < m:
#         volume += n**3
#         if volume == m:
#             return n
#         n += 1
#     return -1


def find_nb(m):
    control_sum = 0
    for i in range(1,m):
        control_sum += i**3
        if control_sum == m:
            return i
        if control_sum > m:
            return -1
