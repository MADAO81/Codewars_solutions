# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python

# quadrant = lambda x, y: ((1,2),(4,3))[y<0][x<0]


def quadrant(x, y):
    if x>0 and y>0:
        return 1
    elif x>0 and y<0:
        return 4
    elif x<0 and y>0:
        return 2
    else:
        return 3
