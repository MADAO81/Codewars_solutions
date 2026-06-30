# https://www.codewars.com/kata/588f5a38ec641b411200005b/train/python

# def how_many_years (date1,date2):
#     year1 = int(date1.split('/')[0])
#     year2 = int(date2.split('/')[0])
#     difference = abs(year1 - year2)
#     return difference


def how_many_years (date1,date2):
    return abs(int(date1.split('/')[0]) - int(date2.split('/')[0]))
