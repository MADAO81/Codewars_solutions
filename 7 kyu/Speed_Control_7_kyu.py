# https://www.codewars.com/kata/56484848ba95170a8000004d/train/python



# def gps(s, x):
#     if len(x) <= 1:
#         return 0
#     res = []
#     for i in range(len(x)-1):
#         res.append((x[i+1]-x[i]) * 3600 / s)
#     return max(res)


def gps(s, x):
    if len(x) < 2:
        return 0
    a = max(x[i] - x[i-1] for i in range(1, len(x))) 
    return a * 3600.0 / s
