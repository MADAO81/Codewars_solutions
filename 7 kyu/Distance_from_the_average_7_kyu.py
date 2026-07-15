# https://www.codewars.com/kata/568ff914fc7a40a18500005c/train/python

# from numpy import mean
# def distances_from_average(test_list):
#     avg = mean(test_list)
#     return [round(avg - x, 2) for x in test_list]



def distances_from_average(test_list):
    if not test_list:
        return []
    average = sum(test_list) / len(test_list)
    return [round(average - value, 2) for value in test_list]
