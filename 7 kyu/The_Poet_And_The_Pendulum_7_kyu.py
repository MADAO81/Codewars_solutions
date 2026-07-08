# https://www.codewars.com/kata/5bd776533a7e2720c40000e5/train/python

# def pendulum(values):
#     sorted_values = sorted(values)
#     result = []
#     for i in range(len(sorted_values)):
#         if i % 2 == 0:
#             result.insert(0, sorted_values[i])
#         else:
#             result.append(sorted_values[i])
#     return result


def pendulum(a):
    a = sorted(a)
    return a[::2][::-1] + a[1::2]
