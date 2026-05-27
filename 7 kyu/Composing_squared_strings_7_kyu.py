# https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

# def compose(s1, s2):
#     lines1 = s1.split('\n')
#     lines2 = s2.split('\n')
#     n = len(lines1)
#     result = []
#     for i in range(n):
#         first_part = lines1[i][:i+1]
#         second_part = lines2[n-1-i][:n-i]
#         result.append(first_part + second_part)
#     return '\n'.join(result)


def compose(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]
    
    n = len(s1)
    out = []
    
    for i in range(n):
        out.append(s1[i][:i+1] + s2[i][:(n-i)])
    
    return "\n".join(out)
