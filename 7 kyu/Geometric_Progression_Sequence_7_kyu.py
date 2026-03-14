# https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python


# def geometric_sequence_elements(a, r, n):
#     l = []
#     for _ in range(n):
#         l.append(str(a))
#         a *= r
#     return ", ".join(l)


def geometric_sequence_elements(a, r, n):
    return ", ".join(str(a*r**i) for i in range(n))
