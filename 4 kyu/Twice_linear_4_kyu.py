# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

# Example:
# dbl_linear(10) should return 22

# Note:
# Focus attention on efficiency

# def dbl_linear(n):
#     u = [1]
#     i2 = i3 = 0

#     for _ in range(n):
#         y = 2 * u[i2] + 1
#         z = 3 * u[i3] + 1
#         next_val = min(y, z)
#         u.append(next_val)

#         if next_val == y:
#             i2 += 1
#         if next_val == z:
#             i3 += 1

#     return u[n]


def dbl_linear(n):
  num_list = [1]
  for i in num_list:
    num_list.append((i * 2) + 1)
    num_list.append((i * 3) + 1)
    if len(num_list) > n *10:
      break
  return sorted(list(set(num_list)))[n]
