# https://www.codewars.com/kata/5601c5f6ba804403c7000004/train/python


def bar_triang(point_a, point_b, point_c): 
    x = round(((point_a[0]+point_b[0]+point_c[0])/3),4)
    y = round(((point_a[1]+point_b[1]+point_c[1])/3),4)
    return [x,y]


# def bar_triang(a, b, c):
#     return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]
