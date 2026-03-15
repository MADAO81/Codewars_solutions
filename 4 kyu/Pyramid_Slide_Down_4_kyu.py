# https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python

# def longest_slide_down(pyramid):
#     for row in range(len(pyramid) -2, -1, -1):
#         for i in range(len(pyramid[row])):
#             pyramid[row][i] += max(pyramid[row+1][i], pyramid[row+1][i+1])
#     return pyramid[0][0]

def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()
