# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

# def max_rot(n):
#     maximum = n
#     s = list(str(n))
#     for i in range(len(s)-1):
#         s.append(s.pop(i))
#         current = int("".join(s))
#         if current > maximum:
#             maximum = current
#     return maximum


def max_rot(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)
